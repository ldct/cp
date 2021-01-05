#include <bits/stdc++.h>
using namespace std;

constexpr int MAX_N = 200009;
int N;
int arr[MAX_N];
int memo[MAX_N];

int ans(int i) {
  if (i >= N) return 0;
  if (memo[i] != -1) return memo[i];
  return memo[i] = arr[i] + ans(i + arr[i]);
}

int main() {

  int T;
  cin >> T;
  while (T--) {
    cin >> N;
    for (int i=0; i<N; i++) {
      cin >> arr[i];
    }
    for (int i=0; i<N+5; i++) {
      memo[i] = -1;
    }
    int ret = -1;
    for (int i=0; i<N; i++) {
      ret = max(ret, ans(i));
    }
    cout << ret << endl;
  }

  return 0;
}
