#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

int T, N;

int main() {

  cin >> T;
  while (T --> 0) {
    cin >> N;
    vector<int> xs;
    vector<int> ys;
    for (int i=0; i<2*N; i++) {
      int x, y;
      cin >> x >> y;
      if (x == 0) ys.push_back(abs(y));
      if (y == 0) xs.push_back(abs(x));
    }
    sort(xs.begin(), xs.end());
    sort(ys.begin(), ys.end());
    double ret = 0.0;
    for (int i=0; i<N; i++) {
      int x = xs[i];
      int y = ys[i];
      ret += sqrt(x*x + y*y);
    }
    cout << setprecision(15) << ret << endl;
  }

  return 0;
}
