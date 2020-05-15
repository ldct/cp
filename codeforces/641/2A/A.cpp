#include <cstdio>

int ans(int N, int K) {
  if (N % 2 == 0) {
    return N + 2*K;
  } else {
    for (int d = 3;; d++) {
      if (N % d == 0) {
        return ans(N+d, K-1);
      }
    }
  }
}

int main() {
  
  int T;

  scanf("%d", &T);

  for (int t=0; t<T; t++) {
    int N, K;
    scanf("%d %d\n", &N, &K);
    printf("%d\n", ans(N, K));
  }
  
  return 0;
}
