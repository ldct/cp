#include <bits/stdc++.h>
using namespace std;

// computes sigma_1(n) for all 1 <= n <= 10^7
// 0.3s

const int N = (int) 1e7 + 100;

long long s[N];
int d[N];

int main() {
  fill(d, d + N, -1);
  d[1] = 1;
  for (int i = 2; i * i < N; i++) {
    if (d[i] == -1) {
      d[i] = i;
      for (int j = i * i; j < N; j += i) {
        if (d[j] == -1) {
          d[j] = i;
        }
      }
    }
  }
  s[1] = 1;
  for (int i = 2; i < N; i++) {
    if (d[i] == -1) {
      d[i] = i;
      s[i] = i + 1;
    } else {
      int j = i;
      s[i] = 1;
      while (j % d[i] == 0) {
        j /= d[i];
        s[i] = s[i] * d[i] + 1;
      }
      s[i] *= s[j];
    }
  }
  for (int i=0; i<20; i++) cout << s[i] << " ";
  cout << endl;
}