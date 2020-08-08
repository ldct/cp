#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_NM = 2009;

int N, M;
char grid[MAX_NM][MAX_NM];

long long memo[MAX_NM][MAX_NM];

long long max_at(char c, int x, int y) {
  if (!(0 <= x && x < N)) return 0;
  if (!(0 <= y && y < M)) return 0;
  if (grid[x][y] != c) return 0;

  if (memo[x][y] != -1) {
    // cout << x << " " << y << " returning" << memo[x][y] << endl;
    return memo[x][y];
  }

  memo[x][y] = 1+min(
    min(
      max_at(c, x, y-1),
      max_at(c, x, y-2)
    ),
    min(
      max_at(c, x-1, y-1),
      max_at(c, x+1, y-1)
    )
  );
  // cout << x << " " << y << " setting" << memo[c-'a'][x][y] << endl;

  return memo[x][y];
}

int main() {

  cin >> N >> M;

  for (int i=0; i<N; i++) {
    for (int j=0; j<M; j++) {
      char c;
      cin >> c;
      assert('a' <= c && c <= 'z');
      grid[i][j] = c;
    }
  }

  long long ret = 0;

  for (char c = 'a'; c <= 'z'; c++) {

    memset(memo, -1, sizeof(memo));

    for (int i=0; i<N; i++) {
      for (int j=0; j<M; j++) {
        ret += max_at(c, i, j);
      }
    }
  }

  cout << ret << endl;


    
  return 0;
}
