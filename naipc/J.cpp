#include <cstdio>
#include <cmath>

int max(int a, int b) {
  if (a > b) {
    return a;
  } else {
    return b;
  }
}

int abs(int a) {
  return max(a, -a);
}

// a_1 a_2 ... a_n
// a_1 = first_char
int max_score(int first_char, int n) {
  if (n <= 1) {
    return 0;
  }
  int first_sum = max(25 - first_char, first_char);
  return first_sum + 25 * (n - 2);
}

int main() {

  int k;
  scanf("%d", &k);
  int n = ceil((float) k / 25) + 1;

  int target = k;
  int prev = 0;
  n--;

  printf("a");

  while (target > 0) {
    for (int i=0; i<=25; i++) {
      if (abs(prev - i) + max_score(i, n) >= target && target - abs(prev - i) >= 0) {
        printf("%c", 'a' + i);
        target -= abs(prev - i);
        prev = i;
        n--;
        break;
      }
    }
  }
  printf("\n");

  return 0;
}
