#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

constexpr int MODULUS = 1000000007;

int T, K;

int memo[100009];
int prefix[100009];

int ans(int l) {
  if (l == 0) return 1;
  if (l < 0) return 0;

  if (memo[l] != -1) return memo[l];

  return memo[l] = (ans(l-1) + ans(l-K)) % MODULUS;
}

i32 main() {

  memset(memo, -1, sizeof(memo));

  cin >> T >> K;

  prefix[0] = 0;
  for (int i=1; i<100008; i++) {
    prefix[i] = (prefix[i-1] + ans(i)) % MODULUS;
  }


  for (int i=0; i<T; i++) {
    int a, b;
    cin >> a >> b;
    cout << ((prefix[b] - prefix[a-1] + MODULUS) % MODULUS) << endl;
  }

  return 0;
}
