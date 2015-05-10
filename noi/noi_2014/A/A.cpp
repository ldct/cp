#include <cstdio>

#define MAX_N 150
#define MAX_M 5000

int N, M;
int orchard[MAX_N][MAX_M];
int prefix[MAX_N][MAX_M+1];
int row_prefix[MAX_N+1][MAX_M+1];

int min(int a, int b) {
  return a > b ? b : a;
}

int max(int a, int b) {
  return a > b ? a : b;
}

int main() {

  scanf("%d %d\n", &N, &M);

  int total_I = 0;

  for (int i=0; i<N; i++) {
    for (int j=0; j<M; j++) {
      scanf("%d", &orchard[i][j]);
      if (orchard[i][j] == 0) {
        orchard[i][j] = -1;
      } else {
        total_I++;
      }
    }
  }

  // for (int i=0; i<N; i++) {
  //   for (int j=0; j<M; j++) {
  //     printf("%+d ", orchard[i][j]);
  //   }
  //   printf("\n");
  // }
  // printf("\n");

  for (int I=0; I<N; I++) {
    row_prefix[I][0] = 0;
  }

  for (int I=0; I<N; I++) {
    for (int j=1; j<=M; j++) {
      row_prefix[I][j] = orchard[I][j-1] + row_prefix[I][j - 1];
    }
  }

  // for (int i=0; i<N; i++) {
  //   for (int j=0; j<=M; j++) {
  //     printf("%+d ", row_prefix[i][j]);
  //   }
  //   printf("\n");
  // }

  for (int j=0; j<=M; j++) {
    prefix[0][j] = 0;
  }

  for (int j=1; j<=M; j++) {
    for (int i=1; i<=N; i++) {
      prefix[i][j] = row_prefix[i-1][j] + prefix[i-1][j];
    }
  }

  // printf("\n");

  // for (int i=0; i<=N; i++) {
  //   for (int j=0; j<=M; j++) {
  //     printf("%+d ", prefix[i][j]);
  //   }
  //   printf("\n");
  // }

  #define f(x) (prefix[I][(x)] - prefix[i][(x)])

  int max_max_diff = 0;

  for (int i=0; i<=N; i++) {
    for (int I=i+1; I<=N; I++) {
      int min_so_far = f(0);
      int max_diff = 0;
      for (int j=0; j<M; j++) {
        int diff = f(j) - min_so_far;

        min_so_far = min(min_so_far, f(j));
        max_diff = max(max_diff, diff);
      }
      max_max_diff = max(max_max_diff, max_diff);
    }
  }

  printf("%d\n", total_I - max_max_diff);

  return 0;
}
