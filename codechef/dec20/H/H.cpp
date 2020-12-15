#include <bits/stdc++.h>
using namespace std;

long long N;
constexpr long long MODULUS = 998244353;
long long A[29];

long long memo[29][240][240];

long long f(long long N, long long B, long long S) {
  if (N == 1) {
    if (B > S) return 1;
    return 0;
  }
  if (memo[N][B][S] != -1) return memo[N][B][S];

  long long ret = 0;
  for (long long b=0; b<B; b++) {
    long long new_S = S - A[N-1]*b;
    new_S %= 239;
    new_S += 239;
    new_S %= 239;

    ret += f(N-1, b, new_S);
    ret %= MODULUS;
  }

  return memo[N][B][S] = ret;
}

int main() {

  memset(memo, -1, sizeof(memo));

  cin >> N;

  for (int i=0; i<N; i++) {
    cin >> A[i];
  }

  long long ret = f(N, 239, 0);

  for (long long m = 1; m <= N; m++) {
    ret *= m;
    ret %=  MODULUS;
  }

  cout << ret << endl;


  return 0;
}
