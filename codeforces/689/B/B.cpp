#include <bits/stdc++.h>
using namespace std;

int T;
int N, M;
char grid[509][509];
long long memo[509][509];

long long max_at(int x, int y) {
  if (!(0 <= x && x < N)) return 0;
  if (!(0 <= y && y < M)) return 0;
  if (grid[x][y] != '*') return 0;
  if (x == N-1) return 1;

  if (memo[x][y] != -1) return memo[x][y];
  return memo[x][y] = 1 + min(max_at(x+1, y-1), min(max_at(x+1, y), max_at(x+1, y+1)));
}

int main() {

  cin >> T;

  while (T --> 0) {
    memset(grid, 0, sizeof(grid));
    memset(memo, -1, sizeof(memo));

    cin >> N >> M;
    for (int i=0; i<N; i++) {
      for (int j=0; j<M; j++) {
        cin >> grid[i][j];
        assert(grid[i][j] == '*' || grid[i][j] == '.');
      }
    }

    long long ret = 0;


    for (int i=0; i<N; i++) {
      for (int j=0; j<M; j++) {
        ret += max_at(i, j);
      }
    }

    cout << ret << endl;
  }

  return 0;
}
