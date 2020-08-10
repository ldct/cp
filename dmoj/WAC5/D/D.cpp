#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

int N, Q;

int main() { 
  cin >> N >> Q;
  vector<long long>A(N, 0);
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A[i] = a;
  }

  auto s = SegTree(A, 0, A.size()-1);


  for (int sqrt_sz=1; sqrt_sz*sqrt_sz<= A.size(); sqrt_sz++) {
    int sz = sqrt_sz*sqrt_sz;
    cout << "testing size " << sz << endl;

    for (int i=0; i<A.size(); i++) {
      int j = i+sz-1;
      auto p = s.rangeMin(i, j);
      if (p.second == sqrt_sz) {
        cout << "the range " << i << " " << j << " is good" << endl;
      }

    }

  }

//   for (int i=0; i<M; i++) {
//     int a, b, c;
//     cin >> a >> b >> c;
//     if (a == 1) {
//       s.pointSet(b, c);
//     } else {
//       auto p = s.rangeMin(b, c-1);
//       cout << p.first << " " << p.second << endl;
//     }
//   }

  return 0;
}
