#include <bits/stdc++.h>
using namespace std;

int T, N;

int main() {

  cin >> T;
  while (T --> 0) {
    cin >> N;
    int ret = -1;
    while (N --> 0) {
      int a;
      cin >> a;
      ret = max(ret, a);
    }
    cout << ret << endl;
  }
  return 0;
}
