#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

long long N, X;
vector<long long> A;

long long memo[102][102][102][102];

long long rm(long long x, long long M) { return ((x % M) + M) % M; }
long long mc(int i, int target, int M, int c) {
    if (c < 0) return -1;
    if (i == N) {
      if (target == 0 && c == 0) return 0;
      return -1;
    }

    if (memo[i][target][M][c] != -1) return memo[i][target][M][c];

    long long option1 = mc(i+1, target, M, c);
    long long option2 = mc(i+1, rm(target - A[i], M), M, c-1);

    if (option2 != -1) option2 += A[i];

    if (option1 == -1) return memo[i][target][M][c] = option2;
    if (option2 == -1) return memo[i][target][M][c] = option1;

    return memo[i][target][M][c] = max(option1, option2);
}

int main() {

  cin >> N >> X;

  memset(memo, -1, sizeof(memo));

  for (int i=0; i < N; i++) {
    long long a;
    cin >> a;
    A.push_back(a);
  }

  // cout << 4999999994 << endl; return 0;

  long long best = LLONG_MAX;

  for (long long t=1; t<=N; t++) {
    cout << t << endl;
    long long s = mc(0, X % t, t, t);
    if (s == -1) continue;
    assert((X - s) % t == 0);
    best = min(best, (X - s) / t);
  }

  cout << best << endl;

  return 0;
}
