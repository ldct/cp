#include <cstdio>

#define MAX_N 2000

int N, M;
int B[MAX_N];
int P[MAX_N];

int main() {

  scanf("\n", &N, &M);

  for (int i=0; i<N; i++) {
    scanf("%d %d\n", &B[i], &P[i]);
  }

  prefix[0] = 0;

  for (int i=0; i<=N; i++) {
    prefix[i] = prefix[i-1] + Y[i-1];
  }

  // for (int i=0; i<=N; i++) {
  //   for (int j=0; j<=N; j++) {
  //     minscore_memo[i][j] = -1;
  //   }
  // }

  long long min_so_far = -1;
  for (int x=A; x<=B; x++) {
    min_so_far = min(min_so_far, minscore(x, N, 0), 0);
  }
  printf("%lld\n", min_so_far);

  return 0;
}
