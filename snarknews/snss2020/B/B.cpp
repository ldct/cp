#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

int main() {
  
  long long A,B,C,D,E;
  cin >> A >> B >> C >> D >> E;

  long long ret = A;
  A = 0;

  E -= min(B, E);
  ret += B;
  B = 0;

  // do C,D,E

  ret += C;
  if (D >= C) {
    D -= C;
    C = 0;
  } else {
    long long slots = C - D;
    E -= 2*slots;
    E = max(E, 0LL);
    C = D = 0;    
  }
  
  long long pairs = D / 2;
  E -= min(pairs, E);
  D -= 2*pairs;
  ret += pairs;

  // cout << "D=" << D << "E=" << E << "ret=" << ret << endl;

  if (D > 0) {
    assert(D == 1);
    E -= min(E, 3LL);
    ret += 1;
    D = 0;
  }

  ret += E/5;
  E -= 5*(E/5);

  if (E > 0) {
    assert(E < 5);
    ret += 1;
    E = 0;
  }

  cout << ret << endl;

  return 0;
}
