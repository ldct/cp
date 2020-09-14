#include <iostream>
using namespace std;

constexpr int MODULUS = 1000000007;
long long S;

long long memo[2009];

long long ans(long long S) {
  if (S == 3) return 1;
  if (S < 3) return 0;

  if (memo[S] != -1) return memo[S];

  long long ret = 1;
  for (int i=3; i<S; i++) {
    ret += ans(S-i);
    ret %= MODULUS;
  }
  return memo[S] = ret;
}

int main() {

  for (int i=0; i<2009; i++) memo[i] = -1;
  
  cin >> S;
  long long r = ans(S);
  r %= MODULUS;
  r += MODULUS;
  r %= MODULUS;

  cout << r << endl;

  return 0;
}
