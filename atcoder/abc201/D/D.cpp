#include <bits/stdc++.h>
using namespace std;

int H, W;
char grid[2009][2009];
int memo[2009][2009];
int INF = 10000000;
int MARKER = 2*INF;

int score(int x, int y) {
  if (grid[x][y] == '+') return 1;
  if (grid[x][y] == '-') return -1;
  assert(false);
}

int p1_advantage(int x, int y) {

  if (memo[x][y] != MARKER) return memo[x][y];

  int px = -INF;
  int py = -INF;

  if (x + 1 < H) px = score(x+1, y) - p1_advantage(x+1, y);
  if (y + 1 < W) py = score(x, y+1) - p1_advantage(x, y+1);

  if (px == -INF && py == -INF) return memo[x][y] = 0;

  return memo[x][y] = max(px, py);
}

int main() {

  cin >> H >> W;
  for (int i=0; i<H; i++) for (int j=0; j<W; j++) {
    cin >> grid[i][j];
    memo[i][j] = MARKER;
  }

  for (int i=0; i<H; i++) for (int j=0; j<W; j++) {
    char c = grid[i][j];
    assert(c == '+' || c == '-');
  }

  int r = p1_advantage(0, 0);

  if (r == 0) cout << "Draw" << endl;
  if (r > 0) cout << "Takahashi" << endl;
  if (r < 0) cout << "Aoki" << endl;

  return 0;
}
