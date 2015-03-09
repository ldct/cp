#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

#define MAX_N 2000
#define MAX_D 20

int N, D;
int p[MAX_N];
long long prefix_p[MAX_N + 1];
long long memo[MAX_N][MAX_D];

long long f(int i, int j) {
    int sum = prefix_p[j] - prefix_p[i];

    if (sum % 10 <= 4) {
        return sum - (sum % 10);
    } else {
        return sum - (sum % 10) + 10;
    }
}

long long dp(int n, int d) {
    if (n == 0) {
        return 0;
    } else if (memo[n][d] != -1) {
        return memo[n][d];
    } else if (d == 0) {
        memo[n][d] = f(0, n);
        return memo[n][d];
    } else {
        long long min_c = dp(0, d - 1) + f(0, n);
        for (int k=0; k <= n; k++) {
            min_c = min(min_c, dp(k, d - 1) + f(k, n));
        }
        memo[n][d] = min_c;
        return min_c;
    }
}

int main() {

  scanf("%d %d", &N, &D);

  memset(memo, -1, sizeof(memo));

  for (int i=0; i<N; i++) {
    scanf("%d", &p[i]);
    if (i == 0) {
        prefix_p[i] = 0;
    } else {
        prefix_p[i] = p[i - 1] + prefix_p[i - 1];
    }
    prefix_p[N] = p[N - 1] + prefix_p[N - 1];
  }

  // for (int i=0; i<N; i++) {
  //   printf("%d:%d\n", i, p[i]);
  // }

  printf("%lld\n", dp(N, D));

  return 0;
}
