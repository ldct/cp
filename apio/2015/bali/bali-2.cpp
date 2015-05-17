#include <cstdio>

#define MAX_N 50
#define MAX_Y 10

/*

Test Case 2

*/

int N, A, B;
int Y[MAX_N];
int prefix[MAX_N+1];

long long min(long long a, long long b) {
  if (a == -1) return b;
  if (b == -1) return a;
  return a > b ? b : a;
}

bool possible(int curpos, int curOR, int curpartition) {
  // printf("%d %d %d\n", curpos, curOR, curpartition);
  if (curpartition == 0) {
    return curpos == 0;
  } else {
    for (int i=0; i<curpos; i++) {
      for (int o=0; o<=N*MAX_Y; o++) {
        if ((curOR == ((prefix[curpos] - prefix[i]) | o )) && possible(i, o, curpartition - 1)) {
          return true;
        }
      }
    }
  }
  return false;
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

  for (int X=0; X<= MAX_N*MAX_Y; X++) {
    for (int P=A; P<=B; P++) {
      if (possible(N, X, P)) {
        printf("%d\n", X);
        return 0;
      }
    }
  }
  return 0;
}
