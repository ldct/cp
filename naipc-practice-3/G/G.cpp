#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

#define MAX_n 155
#define MAX_c 80

int N;
int n;

int s[MAX_n];
double w[MAX_n];

double memo[MAX_n][MAX_c];
int memo_set[MAX_n][MAX_c];

double max_weight(int k, int c) {

  // max weight formed by choosing subset of parties [0...k)
  // with at least c members

  if (k == 0 && c <= 0) {
    return 1.0;
  } else if (k == 0 && c > 0) {
    return 0.0;
  } else if (memo_set[k][c] == 1) {
    return memo[k][c];
  } else {
    memo_set[k][c] = 1;
    memo[k][c] = max(max_weight(k - 1, c), w[k - 1] * max_weight(k - 1, c - s[k - 1]));
    return memo[k][c];
  }
}

int main() {

  scanf("%d", &N);

  while (N--) {

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
      int p;
      scanf("%d %d\n", &s[i], &p);
      w[i] = (double) p / 100.0;
    }

    memset(memo_set, 0, sizeof(memo_set));

    printf("%.16lf\n", 100 * max_weight(n, 76));
  }

  return 0;
}
