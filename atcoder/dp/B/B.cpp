#include <bits/stdc++.h>

using namespace std;

constexpr size_t MAX_N = 100009;
int N, K;
long long H[MAX_N];
long long memo[MAX_N];

long long cost(int i) {
  if (i == N-1) return 0;
  if (i >= N) return LLONG_MAX;

  if (memo[i] != -1) return memo[i];

  long long ret = LLONG_MAX;
  for (int j=1; j<=K; j++) {
    if (i+j < N) {
      ret = min(ret, abs(H[i] - H[i+j]) + cost(i+j));
    }
  }

  return memo[i] = ret;
}

int main() {

  cin >> N >> K;
  
  for (int i=0; i<N; i++) {
    memo[i] = -1;
  }

  for (int i=0; i<N; i++) {
    cin >> H[i];
  }

  cout << cost(0) << endl;
  
  return 0;
}
