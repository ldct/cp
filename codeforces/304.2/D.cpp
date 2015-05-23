#include <cstdio>
#include <vector>

#define MAX_N 5000010
int prime[MAX_N];
int num_factors_memo[MAX_N];
int num_factors_prefix[MAX_N+1];

using namespace std;

vector<int> primes;

int solve(int a, int b) {
  return 1;
}

int num_factors(int n) {

  if (num_factors_memo[n] != -1) {
    return num_factors_memo[n];
  }

  for (int i=0; i<primes.size(); i++) {
    int candidate = primes[i];
    if (candidate * candidate > n) {
      num_factors_memo[n] = 1;
      return 1;
    } else if (n % candidate == 0) {
      num_factors_memo[n] = (1 + num_factors(n / candidate));
      return num_factors_memo[n];
    }
  }
}

int main() {

  int i = 2;
  for (int i=0; i<MAX_N; i++) {
    prime[i] = 1;
  }
  for (int i=2; i<MAX_N; i++) {
    if (prime[i]) {
      primes.push_back(i);
      for (int j=2*i; j<MAX_N; j+= i) {
        prime[j] = 0;
      }
    }
  }

  for (int i=0; i<MAX_N; i++) {
    num_factors_memo[i] = -1;
  }

  num_factors_prefix[0] = 0;

  for (int i=1; i<MAX_N+1; i++) {
    num_factors_prefix[i] = num_factors_prefix[i - 1] + num_factors(i - 1);
  }

  int T;
  scanf("%d\n", &T);

  while (T--) {

    int a, b;
    scanf("%d %d\n", &a, &b);

    printf("%d\n", num_factors_prefix[a+1] - num_factors_prefix[b+1]);

  }


  return 0;
}
