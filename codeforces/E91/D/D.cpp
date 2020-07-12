#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 200009;

int N, M, X, K, Y;

int A[MAX_N];
int B[MAX_N];

long long ans(int a, int b, long long destroyer) {
  // best cost to match A[a:] and B[b:]

  if (a == N && b == M) return 0;

  long long ret = 2000000009;

  if (a < N && b < M && A[a] == B[b]) ret = min(ret, ans(a+1, b+1, A[a])); // match first two characters
  if (a + K <= N) ret = min(ret, X+ans(a+K, b, destroyer));
  if (a + 1 <= N && destroyer >= A[a]) ret = min(ret, Y+ans(a+1, b, destroyer));
  if (a + 2 <= N && A[a] >= A[a+1]) ret = min(ret, Y+ans(a+1, b, A[a]));
  if (a + 2 <= N && A[a] <= A[a+1]) ret = min(ret, Y+ans(a+2, b, A[a+1]));

  if (ret >= 2000000000) {
    ret = 2000000000;
  }
  return ret;
}

int main() {
  
  cin >> N >> M >> X >> K >> Y;

  for (int i=0; i<N; i++) cin >> A[i];
  for (int i=0; i<M; i++) cin >> B[i];

  cout << ans(0, 0, LLONG_MIN) << endl;

  return 0;
}
