#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

constexpr int MODULUS = 100000000;
int N1, N2, K1, K2;

int memo[109][109][11][11];

int ans(int n1, int n2, int k1, int k2) {
  if (n1 == 0 && n2 == 0) return 1;

  int& slot = memo[n1][n2][k1][k2];
  if (slot != -1) return slot;

  int ret = 0;

  if (n1 > 0 && k1 > 0) ret += ans(n1-1, n2, k1-1, K2);
  if (n2 > 0 && k2 > 0) ret += ans(n1, n2-1, K1, k2-1);

  return slot = (ret % MODULUS);
}

i32 main() {

  memset(memo, -1, sizeof(memo));

  cin >> N1 >> N2 >> K1 >> K2;

  cout << ans(N1, N2, K1, K2) << endl;
  return 0;
}
