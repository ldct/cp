#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

constexpr int MODULUS = 1000000007;

long long modexp(long long b, long long e) {
	long long ans = 1;
	for (; e; b = b * b % MODULUS, e /= 2)
		if (e & 1) ans = ans * b % MODULUS;
	return ans;
}

long long modinv(int a, int b) {
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

vector<pair<int, int>> factorize(int n) {
  vector<pair<int, int>> ret;
  int p = 2;
  while (n > 1) {
    if (p * p > n) {
      ret.push_back({n, 1});
      return ret;
    }
    int e = 0;
    while (n % p == 0) {
      n /= p;
      e++;
    }
    if (e > 0) {
      ret.push_back({p, e});
    }
    p++;
  }
  return ret;
}