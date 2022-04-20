#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int N, MODULUS;

int memo[3009][3009][2][2];

int ans(int target_d, int i, bool has_leak, bool two_parts) {
  if (target_d < 0) return 0;
  if (i == N-1) {
    if (two_parts) return 0;
    if (target_d == 0) return 1;
    return 0;
  }

  if (memo[target_d][i][has_leak][two_parts] != -1) return memo[target_d][i][has_leak][two_parts];

  int ret = 0;

  // add a complete cap
  ret += ans(target_d, i+1, false, false);
  // add a _|
  if (not two_parts)
      ret += 2*ans(target_d-1, i+1, false, false);

  // add a =
  ret += ans(target_d-1, i+1, has_leak, two_parts);


  // add a _
  if ((!has_leak) && (!two_parts))
      ret += 2*ans(target_d-2, i+1, true, true);

  return memo[target_d][i][has_leak][two_parts] = ret % MODULUS;
}

i32 main() {

  memset(memo, -1, sizeof(memo));

  cin >> N >> MODULUS;

  vector<int> ret;

  for (int d=1; d<N; d++) {
    int a = ans(d-1, 0, true, true);
    int b = ans(d, 0, false, false);
    ret.push_back((a + b) % MODULUS);
  }

  for (auto r : ret) {
    cout << r << " ";
  }
  cout << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS