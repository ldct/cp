#include <bits/stdc++.h>
using namespace std;

constexpr int MAX_N = 1000009;
int ans[MAX_N];

int main() {

  ans[0] = 0;
  for (int i=1;i<MAX_N; i++) {
    ans[i] = MAX_N;
  }

  for (int i=0; i<MAX_N; i++) {
    for (char c : to_string(i)) {
      int x = c - '0';
      if (x > 0 && i - x >= 0) ans[i] = min(ans[i], 1 + ans[i - x]);
    }
  }

  int N;
  cin >> N;
  cout << ans[N] << endl;

  return 0;
}
