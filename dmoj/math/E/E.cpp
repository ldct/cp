#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>

using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

constexpr int MODULUS = 1000000007;

int N;
int memo[1000009];

int a(i32 n) {
  if (n == 1) return 1;
  if (n == 2) return 2;
  if (n == 3) return 3;
  if (n == 4) return 5;

  if (memo[n] != -1) return memo[n];
  return memo[n] = (a(n-2) + a(n-3) + a(n-4) + 2) % MODULUS;
}

i32 main() {

  memset(memo, -1, sizeof(memo));
  cin >> N;
  cout << a(N) << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS