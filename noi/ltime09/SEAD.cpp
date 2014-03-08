#include <cstdio>
#include <algorithm>

#define MAX_N 100000
#define P 1000000007
int a[MAX_N];

using namespace std;

int pow(int base, int exponent) {
  if (exponent == 0) return 1;
  if (exponent % 2 == 0) {
    int s = pow(base, exponent / 2);
    return s*s % P;
  }
  if (exponent % 2 == 1) {
    return (pow(base, exponent - 1) * base) % P;
  }
}

int main() {
  int T;
  scanf("%d", &T);

  while (T-->0) {
    int N;
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
      scanf("%d", &a[i]);
    }
    int max_a = a[0];
    for (int i=0; i<N; i++) {
      max_a = max(max_a, a[i]);
    }
    int no_max = 0;
    for (int i=0; i<N; i++) {
      if (a[i] == max_a) {
        no_max++;
      }
    }
    printf("%d\n", pow(2,no_max ) - 1);
  }
}