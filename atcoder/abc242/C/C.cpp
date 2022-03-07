#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

constexpr int MODULUS = 998244353;

vector<int> neighbours(int d) {
  if (d == 1) return {1, 2};
  if (d == 9) return {8, 9};
  return {d-1, d, d+1};
}

int memo[1000009][10];

int dp(int N, int d) {
  if (N == 1) return 1;
  if (memo[N][d] != -1) return memo[N][d];
  int ret = 0;
  for (auto n : neighbours(d)) {
    ret += dp(N-1, n);
    ret %= MODULUS;
  }
  return memo[N][d] = ret;
}

int ans(int N) {
  int ret = 0;
  for (int d=1; d<=9; d++) {
    ret += dp(N, d);
    ret %= MODULUS;
  }
  return ret;
}

int N;

i32 main() {

  memset(memo, -1, sizeof(memo));

  cin >> N;
  cout << ans(N) << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS