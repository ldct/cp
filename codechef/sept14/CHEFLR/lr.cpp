#include <cstdio>

int main() {

  int T;
  char line[100001];
  int P = 1000000007;

  scanf("%d", &T);

  while (T--) {
    scanf("%s", line);

    char* c = line;
    bool oddp = true;
    int i = 1;

    while (*c) {

      if (oddp) {
        if (*c == 'l') {
          i = 2 * i;
        } else {
          i = 2 * i + 2;
        }
      } else {
        if (*c == 'l') {
          i = 2 * i - 1;
        } else {
          i = 2 * i + 1;
        }
      }

      i = i % P;
      c++;
      oddp = !oddp;
    }
    printf("%d\n", i);

  }

  return 0;
}
