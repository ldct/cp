#include <bits/stdc++.h>
using namespace std;

constexpr int MAX_N = 5009;
int N;
int A[MAX_N];
int B[MAX_N];
int C[MAX_N];
long long memo[MAX_N];

long long min3(long long x, long long y, long long z) {
  return min(min(x, y), z);
}

long long ans(int i) {
  if (i == N) return 0;
  if (i == N-1) return A[i];
  if (i == N-2) return min(
    A[i] + A[i+1],
    B[i]
  );
  if (memo[i] != -1) return memo[i];
  return memo[i] = min3(
    A[i] + ans(i+1),
    B[i] + ans(i+2),
    C[i] + ans(i+3)
  );
}

int main() {

  cin >> N;

  for (int i=0; i<N; i++) {
    cin >> A[i] >> B[i] >> C[i];
    memo[i] = -1;
  }

  cout << ans(0) << endl;

  return 0;
}
