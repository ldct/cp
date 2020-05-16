#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_N 100002

int gcd(int a, int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}

int lcm(int a, int b) {
  return (a*b) / gcd(a, b);
}

int a[MAX_N];

int main() {
  
  int N;

  scanf("%d", &N);

  for (int i=0; i<N; i++) {
    scanf("%d", &a[i]);
  }


  int g = a[0];
  for (int i=0; i<N; i++) {
    g = gcd(g, a[i]);
  }

  printf("%d\n", g);
  
  return 0;
}
