#include <bits/stdc++.h>
using namespace std;

int T;
string gS;
constexpr int INF = 1000009;

int match(int i, int k) {
  assert(0 <= k && k <= 2);
  if (k == 0) return gS[i] == 'R' ? 0 : 1;
  if (k == 1) return gS[i] == 'W' ? 0 : 1;
  if (k == 2) return gS[i] == 'R' ? 0 : 1;
  assert(false);
}

int memo[750009][3];

int dp(int i, int k) {
  // cout << "dp" << i << k << endl;
  if (i == gS.size()) {
    if (k == 3) return 0;
    return INF;
  }
  if (k >= 3) return INF;
  if (memo[i][k] != -1) return memo[i][k];
  return memo[i][k] = match(i, k) + min(
    dp(i+1, k),
    dp(i+1, k+1)
  );
}

int ans(string S) {
  gS = S;
  memset(memo, -1, sizeof(memo));
  return dp(0, 0);
}

int main() {
  cin >> T;
  while (T --> 0) {
    int N;
    cin >> N;
    string S;
    cin >> S;
    cout << ans(S) << endl;
  }
  return 0;
}
