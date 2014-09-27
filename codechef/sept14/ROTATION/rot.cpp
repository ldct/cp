#include <cstdio>

int main() {

  int N, M;
  int A[100001];

  scanf("%d %d", &N, &M);

  for (int i=0; i<N; i++) {
    scanf("%d", &A[i]);
  }
  scanf("\n");

  int head = 0;

  while (M--) {
    char query;
    int d;

    scanf("%c %d\n", &query, &d);

    if (query == 'R') {
      printf("%d\n", A[(head + d - 1) % N]);
    } else if (query == 'C') {
      head = (head + d) % N;
    } else if (query == 'A') {
      head = (head - d + N) % N;
    }

  }

  return 0;
}
