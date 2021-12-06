#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

constexpr int MODULUS = 998244353;

int N;
vector<i32> S;

map<tuple<i32, bool, i32>, i32> memo;

int dp(i32 mex_before, bool has_top, i32 i) {
  if (i == S.size()) return 1;
  tuple<i32, bool, i32> key = {mex_before, has_top, i};
  if (memo.count(key)) return memo[key];
  if (has_top) {
    int ret = dp(mex_before, true, i+1);
    if ((S[i] == mex_before-1) || (S[i] == mex_before+1)) ret += dp(mex_before, true, i+1);
    return memo[key] = ret % MODULUS;
  } else {
    int ret = dp(mex_before, false, i+1);
    if (S[i] == mex_before-1) ret += dp(mex_before, false, i+1);
    if (S[i] == mex_before) ret += dp(mex_before+1, false, i+1);
    if (S[i] == mex_before+1) ret += dp(mex_before, true, i+1);
    return memo[key] = ret % MODULUS;
  }
}

i32 main() {

  i32 T;
  cin >> T;
  while (T --> 0) {
    i32 N;
    cin >> N;
    S.clear(); memo.clear();
    while (N --> 0) {
      i32 s;
      cin >> s;
      S.push_back(s);
    }
    cout << (dp(0, false, 0)-1) << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS