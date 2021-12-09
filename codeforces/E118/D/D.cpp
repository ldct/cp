#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>

using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

using namespace __gnu_pbds;

typedef tuple<i32, bool, i32> key_t;

struct key_hash : public unary_function<key_t, size_t>
{
      static uint64_t splitmix64(uint64_t x) {
        // http://xorshift.di.unimi.it/splitmix64.c
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }
 size_t operator()(const key_t& k) const
 {
   return splitmix64(get<0>(k) ^ get<1>(k) ^ get<2>(k));
 }
};

constexpr int MODULUS = 998244353;

int N;
vector<i32> S;

unordered_map<tuple<i32, bool, i32>, i32, key_hash> memo;

int dp(i32 mex_before, bool has_top, i32 i) {
  if (i == S.size()) return 1;
  tuple<i32, bool, i32> key = {mex_before, has_top, i};
  if (memo.find(key) != memo.end()) return memo[key];
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