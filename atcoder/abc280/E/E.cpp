#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>
#include <unordered_map>
#include <cassert>

using namespace std;
#define int long long
#define i32 int32_t
#define i64 int64_t


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

int N, P;
constexpr int MODULUS = 998244353;
int p1, p2;

int memo[200009];

int ans(int S) {
  if (S <= 0) return 0;
  if (memo[S] != -1) return memo[S];
  return memo[S] = (p2*(1 + ans(S-2)) + p1*(1 + ans(S-1))) % MODULUS;
}
        
i32 main() {

  memset(memo, -1, sizeof(memo));
  
  cin >> N >> P;
  p2 = P * modinv(100, MODULUS);
  p2 %= MODULUS;
  p2 += MODULUS;
  p2 %= MODULUS;

  p1 = 1 - p2;
  p1 %= MODULUS;
  p1 += MODULUS;
  p1 %= MODULUS;

  int ret = ans(N);
  ret %= MODULUS; ret += MODULUS; ret %= MODULUS;

  cout << ret << endl;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS