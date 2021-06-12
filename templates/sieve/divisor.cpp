#include <bits/stdc++.h>
using namespace std;

// computes sigma_1(n) for all 1 <= n <= 10^7
// 1s

constexpr size_t MAX_N = 10000007;

int s[MAX_N];

int main() {

  for (int i=1; i<MAX_N; i++)
    for (int j=i; j<MAX_N; j+=i) s[j] += i;

  for (int i=0; i<20; i++) cout << s[i] << " ";
  cout << endl;

  return 0;
}
