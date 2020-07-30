#include <bits/stdc++.h>

using namespace std;

constexpr size_t MAX_N = 1001;
constexpr size_t MAX_M = 1001;

int A[MAX_N][MAX_M];
long long A_p[MAX_N][MAX_M+1];
long long memo[MAX_N][MAX_M];
long long max_containing[MAX_M];

bool all_negative(int N, int M) {
  for (int x=0; x<N; x++) {
    for (int y=0; y<M; y++) {
      if (A[x][y] > 0) return false;
    }
  }
  return true;
}

long long min_from(int x, int y) {
  if (x == 0 && y == 0) return A[x][y];
  if (x == -1) return 0;

  if (memo[x][y] != LLONG_MAX) return memo[x][y];

  if (y == 0) {
    return A[x][y] + min_from(x-1, y);
  }

  long long best = LLONG_MAX;
  for (int y_left=0; y_left<=y; y_left++) {
    for (int y_up=y_left; y_up<=y; y_up++) {
      auto candidate = (A_p[x][y+1] - A_p[x][y_left]) + min_from(x-1, y_up);
      best = min(best, candidate);
    }
  }

  memo[x][y] = best;

  return best;
}

long long best_left(const int x, const int y, const int M) {
  long long ret = LLONG_MAX;
  for (int y_left=0; y_left<=y; y_left++) {
    ret = min(ret, A_p[x][y] - A_p[x][y_left]);
  }
  return ret;
}

long long best_right(const int x, const int y, const int M) {
  long long ret = LLONG_MAX;
  for (int y_right=y;y_right<M; y_right++) {
    ret = min(ret, A_p[x][y_right+1] - A_p[x][y]);
  }
  return ret;
}

int main() {
  
  int N, M;

  cin >> N >> M;

  for (int x=0; x<N; x++) {
    for (int y=0; y<M; y++) {
      int e;
      cin >> e;
      A[x][y] = e;
    }
  } 

  if (all_negative(N, M)) {
    long long ret = 0;
    for (int x=0; x<N; x++) {
      for (int y=0; y<M; y++) {
        ret += A[x][y];
      }
    }
    cout << ret << endl;
    return 0;
  }

  // populate prefix sum
  for (int x=0; x<N; x++) {
    A_p[x][0] = 0;
    for (int y=0; y<M; y++) {
      A_p[x][y+1] = A[x][y] + A_p[x][y];
    }
  }

  if (N == 2) {
    long long best = LLONG_MAX;
    for (int y=0; y<M; y++) {
      best = min(best, A[0][y] + best_left(0, y, M) + best_left(1, y, M) + best_right(1, y, M));
    }
    cout << best << endl;
    return 0;
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
