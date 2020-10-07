#include <bits/stdc++.h>
using namespace std;

// 10 -> 504

constexpr int MODULUS = 12345;

int N;

int memo[100009][3];

int ans(int i, int num_ones) {
  if (i == N) return 1;
  if (memo[i][num_ones] != -1) return memo[i][num_ones];
  if (num_ones == 2) return memo[i][num_ones] = ans(i+1, 0);
  return memo[i][num_ones] = (ans(i+1, 0) + ans(i+1, num_ones+1)) % MODULUS;
}

int main() {

  cin >> N;
  for (int i=0; i<N; i++) for (int j=0; j<3; j++) memo[i][j] = -1;

  cout << ans(0, 0) << endl;
   
  return 0;
}
