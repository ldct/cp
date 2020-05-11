#include <cstdio>

#define MAX_N 8005

int sum[MAX_N];
int a[MAX_N];
bool present[MAX_N];

int main() {
  
  int T;

  scanf("%d", &T);
  for (int t=0; t<T; t++) {
    int N;
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
      scanf("%d", a+i);
    }
    sum[0] = 0;
    for (int i=0; i<N; i++) {
      sum[i+1] = a[i] + sum[i];
    }

    // for (int i=0; i<N; i++) {
    //   printf("%d ", a[i]);
    // }
    // printf("\n");
    // for (int i=0; i<=N; i++) {
    //   printf("%d ", sum[i]);
    // }
    // printf("\n");

    for (int i=0; i<=N; i++) {
      present[i] = false;
    }
    for (int i=0; i<=N-2; i++) {
      for (int j=i+2; j<=N; j++) {
        if (0 < sum[j] - sum[i] && sum[j] - sum[i] <= N) {
          // printf("marking %d\n", sum[j] - sum[i]);
          present[sum[j] - sum[i]] = true;
        }
      }
    }

    // for (int i=1; i<=N; i++) {
    //   printf("%d ", present[i]);
    // }
    // printf("\n");

    int ans = 0;
    for (int i=0; i<N; i++) {
      int target = a[i];
      if (present[target]) {
        // printf("found=%d\n", target);
        ans += 1;
      }
    }
    printf("%d\n", ans);
  }
  
  return 0;
}
