#include <bits/stdc++.h>
using namespace std;

constexpr int MAX_N = 100009;
int N;
string S;
long long memo[MAX_N][2];

bool match(bool is_caps, char c) {
  if (c == ' ') return true;
  return (is_caps && isupper(c)) || (!is_caps && !isupper(c));
}

long long ans(int i, bool is_caps) {
  if (i == N) return 0;
  if (memo[i][is_caps] != -1) return memo[i][is_caps];
  long long ret = LLONG_MAX;
  if (match(is_caps, S[i])) {
    ret = min(ret, 1 + ans(i+1, is_caps));
  } else {
    ret = min(ret, 2 + ans(i+1, is_caps));
    ret = min(ret, 3 + ans(i+1, !is_caps));
  }

  return memo[i][is_caps] = ret;
}

int main() {

  getline(cin, S);
  N = S.size();

  for (int i=0; i<N; i++) {
    memo[i][0] = memo[i][1] = -1;
  }

  cout << ans(0, false) << endl;

  return 0;
}
