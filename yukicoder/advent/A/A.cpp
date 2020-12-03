#include <bits/stdc++.h>
using namespace std;

int N, K, X, Y;
int A_count[1024];
int memo[1024][41][1024];

int ways(int n, int x, int target) {
  // number of ways to make `target` using `x` numbers from [0...n]
  if (x < 0) return 0;
  if (x == 0 || n == 0) {
    if (target == 0) return 1;
    return 0;
  }
  int ret = 0;
  for (int i=0; i<=A_count[n]; i++) {
    if (i % 2 == 0) {
      ret += ways(n-1, x-i, target);
    } else {
      ret += ways(n-1, x-i, target^n);
    }
  }
  return ret;
}

int main() {
  cin >> N >> K >> X >> Y;

  memset(memo, -1, sizeof(memo));
  memset(A_count, 0, sizeof(A_count));

  for (int i=0; i<K; i++) {
    int a;
    cin >> a;
    A_count[a]++;
  }

  int r = 0;

  for (int i=X; i<=Y; i++) {
    cout << i << "\t" << ways(1023, K, i) << endl;
    r += ways(1023, K,i);
  }

  cout << "total\t" << r << endl;

  return 0;
}
