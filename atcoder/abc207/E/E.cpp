#include <bits/stdc++.h>
using namespace std;

int N;
long long A[3009];
long long prefixes[3009];
long long memo[3009][3009];
vector<pair<int, int>> groups[3009];

constexpr int MODULUS = 1000000007;

long long dp(int i, int start) {
  if (i == N) return 1;
  if (memo[i][start] != -1) return memo[i][start];

  long long ret = 0;
  for (const auto p : groups[start]) {
    if (i == p.first) {
      int j = p.second;
      ret += dp(j, start+1);
      ret %= MODULUS;
    }
  }
  return memo[i][start] = ret;
}

long long mod(long long x) {
  x %= MODULUS;
  x += MODULUS;
  x %= MODULUS;
  return x;
}

int main() {

  memset(memo, -1, sizeof(memo));

  cin >> N;
  for (int i=0; i<N; i++) {
    cin >> A[i];
  }

  prefixes[0] = 0;
  for (int i=1; i<=N; i++) prefixes[i] = prefixes[i-1] + A[i-1];

  for (int i=0; i<=N; i++) {
    for (int j=i+1; j<=N; j++) {
      long long m = mod(prefixes[j] - prefixes[i]);
      groups[m].push_back({i, j});
    }
  }

  cout << dp(0, 1) << endl;

  return 0;
}
