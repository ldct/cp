#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> void sort_unique(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()),v.end());}

constexpr int MAX_N = 1000009;
int N;

int memo[MAX_N];

int main() {

  memo[1] = 0;
  for (int i=2; i<MAX_N; i++) {
    int ret = memo[i-1] + 1;
    if (i % 2 == 0) ret = min(ret, 1+memo[i/2]);
    if (i % 3 == 0) ret = min(ret, 1+memo[i/3]);
    memo[i] = ret; 
  }

  int n;
  while (cin >> n) {
    cout << memo[n] << endl;
  }

  return 0;
}
