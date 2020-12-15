#include <bits/stdc++.h>
using namespace std;

int T;

long long count(long long a, long long b) {
  return a*b;
}

long long ans(long long a, long long b) {
  return count(a/2, b/2) + count((a+1)/2, (b+1)/2);
}

int main() {

  cin >> T;

  while (T --> 0) {
    long long A, B;
    cin >> A >> B;
    cout << ans(A, B) << endl;
  }

  return 0;
}
