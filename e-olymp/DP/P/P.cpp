#include <bits/stdc++.h>
using namespace std;

constexpr int MAX_N = 100009;
long long height[MAX_N];
long long ans[MAX_N];

int N;

int main() {

  cin >> N;

  for (int i=0; i<N; i++) {
    ans[i] = LLONG_MAX;
    cin >> height[i];
  }

  ans[N-1] = 0;
  ans[N-2] = abs(height[N-1] - height[N-2]);
  for (int i=N-3; i >= 0; i--) {
    ans[i] = min(
      abs(height[i] - height[i+1]) + ans[i+1],
      abs(height[i] - height[i+2]) + ans[i+2]
    );
  }

  cout << ans[0] << endl;

  return 0;
}
