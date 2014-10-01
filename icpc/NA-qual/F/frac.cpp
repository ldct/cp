#include <cstdio>

int main() {

  int a, b, rem;

  while (1) {
    scanf("%d %d", &a, &b);
    if (a == 0 && b == 0) {
      return 0;
    }

    rem = a % b;

    printf("%d %d / %d\n", (a - rem) / b, rem, b);

  }

  return 0;
}
