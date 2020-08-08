#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_NM = 2009;

int N, M;
char grid[MAX_NM][MAX_NM];

int memo[MAX_NM][MAX_NM];

char opt_grid(int x, int y) {
  if (!(0 <= x && x < N)) return '-';
  if (!(0 <= y && y < M)) return '-';
  return grid[x][y];
}

int max_at(int x, int y) {
  if (!(0 <= x && x < N)) return 0;
  if (!(0 <= y && y < M)) return 0;

  if (memo[x][y] != -1) {
    return memo[x][y];
  }

  char c = grid[x][y];
  if (!(opt_grid(x, y-1) == c)) return 1;
  if (!(opt_grid(x, y-2) == c)) return 1;
  if (!(opt_grid(x-1, y-1) == c)) return 1;
  if (!(opt_grid(x+1, y-1) == c)) return 1;


  memo[x][y] = 1+min(
    min(
      max_at(x, y-1),
      max_at(x, y-2)
    ),
    min(
      max_at(x-1, y-1),
      max_at(x+1, y-1)
    )
  );

  return memo[x][y];
}

int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> M;

  memset(memo, -1, sizeof(memo));

  for (int i=0; i<N; i++) {
    for (int j=0; j<M; j++) {
      char c;
      cin >> c;
      assert('a' <= c && c <= 'z');
      grid[i][j] = c;
    }
  }

  long long ret = 0;

  for (int i=0; i<N; i++) {
    for (int j=0; j<M; j++) {
      // cout << max_at(i, j) << '\t';
      ret += max_at(i, j);
    }
    // cout << endl;
  }
  

  cout << ret << endl;
    
  return 0;
}
