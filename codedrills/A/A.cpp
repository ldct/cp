#include <bits/stdc++.h>
using namespace std;

int totalbottles(int N, int X) {
  int ret = 0;
  int empty = 0;
  for (int i=0; i<10000; i++) {
    if (N == 0 && empty < X) break;
    ret += N;
    empty += N;
    N = empty / X;
    empty %= X;
  }
  return ret;
}

int main() {

  cout << totalbottles(5, 3) << endl;

  return 0;
}
