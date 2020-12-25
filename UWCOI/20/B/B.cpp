#include <bits/stdc++.h>
using namespace std;

int T, N;

int main() {

  cin >> T;
  while (T --> 0) {
    cin >> N;
    long long num_odd = 0;
    long long num_even = 0;
    while (N --> 0) {
      long long a;
      cin >> a;
      if (a % 2 == 0) { num_even++; } else { num_odd++; }
    }
    long long ret = num_odd*num_even;
    cout << ret << endl;
  }
  return 0;
}
