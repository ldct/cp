#include <bits/stdc++.h>
using namespace std;

int H, W;
char grid[2009][2009];
constexpr int MODULUS = 1000000007;

long long ways(int x, int y);
long long ways_left(int x, int y);
long long ways_up(int x, int y);
long long ways_diag(int x, int y);

long long memo[2009][2009];
long long memo_left[2009][2009];
long long memo_up[2009][2009];
long long memo_diag[2009][2009];

long long ways(int x, int y) {
  if (x < 0) return 0;
  if (y < 0) return 0;
  if (grid[x][y] == '#') return 0;
  if (x == 0 && y == 0) return 1;
  if (memo[x][y] != -1) return memo[x][y];
  return memo[x][y] = (ways_left(x-1, y) + ways_up(x, y-1) + ways_diag(x-1, y-1)) % MODULUS;
}

long long ways_left(int x, int y) {
  if (x < 0) return 0;
  if (y < 0) return 0;
  if (grid[x][y] == '#') return 0;
  if (memo_left[x][y] != -1) return memo_left[x][y];

  return memo_left[x][y] = (ways(x, y) + ways_left(x-1, y)) % MODULUS;
}

long long ways_up(int x, int y) {
  if (x < 0) return 0;
  if (y < 0) return 0;
  if (grid[x][y] == '#') return 0;
  if (memo_up[x][y] != -1) return memo_up[x][y];

  return memo_up[x][y] = (ways(x, y) + ways_up(x, y-1)) % MODULUS;
}

long long ways_diag(int x, int y) {
  if (x < 0) return 0;
  if (y < 0) return 0;
  if (grid[x][y] == '#') return 0;
  if (memo_diag[x][y] != -1) return memo_diag[x][y];

  return memo_diag[x][y] = (ways(x, y) + ways_diag(x-1, y-1)) % MODULUS;
}

int main() {

  cin >> H >> W;

  memset(memo, -1, sizeof(memo));
  memset(memo_left, -1, sizeof(memo_left));
  memset(memo_up, -1, sizeof(memo_up));
  memset(memo_diag, -1, sizeof(memo_diag));

  for (int i=0; i<H; i++) for (int j=0; j<W; j++) {
    cin >> grid[i][j];
    assert(grid[i][j] == '#' || grid[i][j] == '.');
  }

  cout << ways(H-1, W-1) << endl;

  return 0;
}
