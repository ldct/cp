#include <cstdio>

#define MAX_N 2000
#define MAX_K 2000

/*

Observation: if it were true that for all a <= b and for all x
a | x <= b | x then we can do this DP
however this is not true...

*/

int N, A, B;
int Y[MAX_N];
int prefix[MAX_N+1];

long long minscore_memo[MAX_K+1][MAX_N+1];

long long min(long long a, long long b, long long mm) {
  if (a == -1) return b;
  if (b == -1) return a;
  return (a | mm) > (b | mm) ? b : a;
}

long long minscore(int k, int n, long long min_metric) {
  if (k == 1) {
    return prefix[n] - prefix[0];
  } else if (n < k) {
    return -1;
  } else {
    long long min_so_far = -1;

    for (int end=0; end<n; end++) {
      long long end_beauty = prefix[n] - prefix[end];
      long long score = minscore(k - 1, end, min_metric | end_beauty) | end_beauty;
      min_so_far = min(min_so_far, score, min_metric);
    }

    minscore_memo[k][n] = min_so_far;
    return min_so_far;
  }
}

int main() {

  scanf("%d %d %d\n", &N, &A, &B);

  for (int i=0; i<N; i++) {
    scanf("%d", &Y[i]);
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
