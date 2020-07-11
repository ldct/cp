#include <bits/stdc++.h>

using namespace std;

constexpr size_t MAX_N = 1000001;
int heights[MAX_N];

int main() {
  
  int N;

  cin >> N;

  for (int i=0; i<N; i++) {
    cin >> heights[i];
  }

  int max_height = -1;
  int max_idx = 0;

  for (int i=0; i<N; i++) {
    auto h = heights[i];
    if (h > max_height) {
      max_height = h;
      max_idx = i;
    }
  }

  int ans = 0;

  max_height = -1;

  for (int i=max_idx-1; i != -1; i--) {
    auto h = heights[i];
    if (h > max_height) {
      ans += 1;
      max_height = h;
    }
  }

  max_height = -1;

  for (int i=max_idx+1; i < N; i++) {
    auto h = heights[i];
    if (h > max_height) {
      ans += 1;
      max_height = h;
    }
  }

  cout << ans << endl;

  return 0;
}
