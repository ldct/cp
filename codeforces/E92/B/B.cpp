#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 200009;
constexpr size_t MAX_Z = 9;

long long A[MAX_N];

long long N, K, Z;

long long memo[MAX_N][MAX_Z][2];

long long ans(int x, int lefts_used, char last_was_left) {

  int moves_used = x + 2*lefts_used;
  if (moves_used == K) return 0;

  if (memo[x][lefts_used][last_was_left] != -1) return memo[x][lefts_used][last_was_left];

  assert(lefts_used <= Z);
  assert(0 <= x && x <= N);

  long long ret = LLONG_MIN;

  // option 1
  if (x < N-1) {
    ret = max(ret, A[x+1] + ans(x+1, lefts_used, false));
  }

  // option 2
  if (x > 0 && !last_was_left && lefts_used < Z) {
    ret = max(ret, A[x-1] + ans(x-1, lefts_used+1, true));
  }

  return memo[x][lefts_used][last_was_left] = ret;

}

int main() {

  int T;
  cin >> T;
  
  while (T --> 0) {
    cin >> N >> K >> Z;

    for (int i=0; i<=N; i++) {
      for (int j=0; j<=Z; j++) {
        memo[i][j][0] = memo[i][j][1] = -1;
      }
    }

    for (int i=0; i<N; i++) {
      cin >> A[i];
    }

    long long r = ans(0, 0, false);
    assert(r >= 0);
    cout << A[0] + ans(0, 0, false) << endl;
  }
    
  return 0;
}
