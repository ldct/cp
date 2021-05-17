#include <bits/stdc++.h>
using namespace std;

int N, T;

void read1() {
  int tmp;
  cin >> tmp;
  assert(tmp == 1);
}

int main() {

  cin >> T >> N;

  while (T --> 0) {
    for (int i=1;i<N;i++) {
      cout << "M " << i << " " << N << endl;
      int j;
      cin >> j;
      if (i == j) continue;
      cout << "S " << i << " " << j << endl;
      read1();
    }
    cout << "D" << endl;
    read1();
  }

  return 0;
}
