#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

int N, M;

int main() {

  cin >> N >> M;
  dsu d(N);

  while (M --> 0) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    d.merge(a, b);
  }

  cout << d.groups().size()-1 << endl;

  return 0;
}
