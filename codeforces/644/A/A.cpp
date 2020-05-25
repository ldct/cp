#include <bits/stdc++.h>

using namespace std;

int ans(int a, int b) {
  if (b < a) return ans(b, a);
  int side = max(2*a, b);
  return side*side;
}

int main() {
  
  int T;

  scanf("%d", &T);

  for (int t=0; t<T; t++) {
    int a, b;
    scanf("%d %d\n", &a, &b);
    printf("%d\n", ans(a, b));
  }

  return 0;
}
