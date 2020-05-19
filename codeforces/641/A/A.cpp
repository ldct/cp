#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_N 100002

int gcd(int a, int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}

unsigned long long lcm(unsigned long long a, unsigned long long b) {
  return (a / gcd(a, b)) * b;
}

int a[MAX_N];
int prefix[MAX_N];
int suffix[MAX_N];
int rest[MAX_N];

int main() {
  
  int N;

  scanf("%d", &N);

  for (int i=0; i<N; i++) {
    scanf("%d", &a[i]);
  }

  prefix[0] = a[0];
  for (int i=1; i<N; i++) {
    prefix[i] = gcd(prefix[i-1], a[i]);
  }

  suffix[N-1] = a[N-1];
  for (int i=N-1; i>=0; i--) {
    suffix[i] = gcd(suffix[i+1], a[i]);    
  }

  rest[0] = suffix[1];
  rest[N-1] = prefix[N-2];

  for (int i=1; i<N-1; i++) {
    rest[i] = gcd(prefix[i-1], suffix[i+1]);
  }

  // for (int i=0; i<N; i++) {
  //   printf("%d ", prefix[i]);
  // }
  // printf("\n");

  // for (int i=0; i<N; i++) {
  //   printf("%d ", suffix[i]);
  // }
  // printf("\n");

  // for (int i=0; i<N; i++) {
  //   printf("%d ", rest[i]);
  // }
  // printf("\n");

  unsigned long long ans = 1;
  for (int i=0; i<N; i++) {
    ans = lcm(ans, rest[i]);
  }

  printf("%llu\n", ans);

  return 0;
}
