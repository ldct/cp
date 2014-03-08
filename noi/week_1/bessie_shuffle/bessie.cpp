#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

#define MAXN 100010

int X[MAXN];
int Y[MAXN];
int PI[MAXN];

void compose(int* R, int* A, int* B, int N) {
  for(int i = 0; i < N; i++) {
    R[i] = A[B[i]];
  }
}

int main() {

  scanf("%d %d %d", &N, &M, &Q);
  int T = N - M + 1;
  for(int i = 0; i < N; i++) {
    X[i] = i;
    if(i < M) {
      int x; 
      scanf("%d", &x);
      x--;
      PI[x] = i;
    } else {
      PI[i] = i;
    }
  }
  rotate(PI, PI + 1, PI + N);

  for(int i = 31 - __builtin_clz(T); i >= 0; i--) {
    compose(Y, X, X, N);
    memcpy(X, Y, sizeof(X));
    if(T & 1 << i) {
      compose(Y, X, PI, N);
      memcpy(X, Y, sizeof(X));
    }
  }
  for(int i = 0; i < Q; i++) {
    int x;
    scanf("%d", &x);

    printf("%d\n", X[(N + M - 1 - x) % N] + 1);
  }
  return 0;
}