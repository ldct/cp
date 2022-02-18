#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

constexpr int MODULUS = 998244353;
int factorial[5009];
int inv[5009];

int modinv(int a, int b) {
	int b0 = b, t, q;
	int x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}

int nCr_mod(int n, int k) {
  if (k == 0) return 1;
  if (k == 1) return n;
  if (n == k) return 1;
  auto ret = factorial[n] * inv[k] % MODULUS * inv[n - k] % MODULUS;
  return ret;
}

string ALPHABET = "abcdefghijklmnopqrstuvwxyz";
int freq[30];

int N;

int memo[30][5009];

int dp(int c, int l) {
  if (l == 0) return 1;
  if (c == -1) return 0;

  if (memo[c][l] != -1) return memo[c][l];

  auto max_num_c = min(l, freq[c]);
  int ret = 0;

  for (int num_c = 0; num_c <= max_num_c; num_c++) {
    ret += (dp(c-1, l-num_c)*nCr_mod(l, num_c)) % MODULUS;
    ret %= MODULUS;
  }
  return memo[c][l] = ret;
}

i32 main() {

  memset(memo, -1, sizeof(memo));

  factorial[0] = 1;
  for (int i = 1; i <= 5000; i++) {
      factorial[i] = factorial[i - 1] * i % MODULUS;
      inv[i] = modinv(factorial[i], MODULUS);
  }

  string S;
  cin >> S;
  for (char c : S) {
    freq[c - 'a']++;
  }

  int ret = 0;
  for (int l=1; l<=S.size(); l++) {
    ret += dp(25, l);
    ret %= MODULUS;
  }
  cout << ret << endl;
  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS