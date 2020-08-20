#include <bits/stdc++.h>

using namespace std;

constexpr size_t MAX_N = 100009;
int N;
long long H[MAX_N][3];
long long memo[MAX_N][3];

long long cost(int i, int choice) {
  if (i == N) return 0;
  assert(i < N);

  if (memo[i][choice] != -1) return memo[i][choice];

  if (choice == 0) return memo[i][0] = H[i][0] + max(cost(i+1, 1), cost(i+1, 2));
  if (choice == 1) return memo[i][1] = H[i][1] + max(cost(i+1, 0), cost(i+1, 2));
  if (choice == 2) return memo[i][2] = H[i][2] + max(cost(i+1, 0), cost(i+1, 1));

  assert(false);

}

int main() {

  cin >> N;
  
  for (int i=0; i<N; i++) {
    memo[i][0] = memo[i][1] = memo[i][2] = -1;
  }

  for (int i=0; i<N; i++) {
    cin >> H[i][0] >> H[i][1] >> H[i][2];
  }

  cout << max(cost(0, 0), max(cost(0, 1), cost(0, 2))) << endl;
  
  return 0;
}
