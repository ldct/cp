#include <bits/stdc++.h>
using namespace std;

constexpr int MODULUS = 1000000007;

int A[100009];
int N;

long long g(int n);

long long f(int n) {
  if (n == 1) return 1;
  return f(n-1) + g(n-1);
}

long long g(int n) {
  if (n == 1) return 0;
  return f(n-1);
}

int main() {


  cout << f(5) + g(5) << endl;
}
