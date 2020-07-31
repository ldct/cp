#include <bits/stdc++.h>

using namespace std;

constexpr size_t MAX_N = 1001;
constexpr size_t MAX_M = 1001;

int A[MAX_N][MAX_M];
long long A_p[MAX_N][MAX_M+1];
long long memo[MAX_N][MAX_M];
long long max_containing[MAX_M];

int N, M;

long long best_left(const int x, const int y) {
  long long ret = LLONG_MAX;
  for (int y_left=0; y_left<=y; y_left++) {
    ret = min(ret, A_p[x][y] - A_p[x][y_left]);
  }
  return ret;
}

long long min_from(int x, int y) {
  if (x == 0 && y == 0) return A[x][y];
  if (x == -1) return 0;
  if (x == 0) return A[x][y] + best_left(0, y);
  if (memo[x][y] != LLONG_MAX) return memo[x][y];

  if (y == 0) {
    return A[x][y] + min_from(x-1, y);
  }

  long long v = best_left(x, y) + A[x][y];

  return memo[x][y] = min(
    min_from(x, y-1) + A[x][y],
    min_from(x-1, y) + v
  );
}

int main() {
  
  cin >> N >> M;

  for (int x=0; x<N; x++) {
    for (int y=0; y<M; y++) {
      int e;
      cin >> e;
      A[x][y] = e;
    }
  } 

  // populate prefix sum
  for (int x=0; x<N; x++) {
    A_p[x][0] = 0;
    for (int y=0; y<M; y++) {
      A_p[x][y+1] = A[x][y] + A_p[x][y];
    }
  }

  //populate memo
    for (int x=0; x<N; x++) {
    for (int y=0; y<M; y++) {
      memo[x][y] = LLONG_MAX;
    }
  }

  long long best = LLONG_MAX;

  for (int y=0; y<M; y++) {
    best = min(best, min_from(N-1,y));
  }
  cout << best << endl;

  return 0;
}
