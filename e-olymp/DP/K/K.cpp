#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> void sort_unique(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()),v.end());}
template<class T, class U> T round_div(const T n, const U d) { return ((n < 0) ^ (d < 0)) ? ((n - d/2)/d) : ((n + d/2)/d); }

constexpr int MAX_N = 39;
int N, K;
long long memo[MAX_N];

long long F(int n, int k) {
  if (n < 0) return 0;
  if (n == 0) return 1;
  if (memo[n] != -1) return memo[n];

  long long ret = 0;
  for (int i=1; i<=k; i++) {
    ret += F(n-i, k);
  }
  return memo[n] = ret;
}

int main() {

  cin >> N >> K;

  for (int i=0; i<N; i++) memo[i] = -1;
  cout << F(N-1, K) << endl;

  return 0;
}
