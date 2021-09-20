#include <bits/stdc++.h>
using namespace std;

int N, X, Y;
int memo[309][309][309];

int xs[309];
int ys[309];

int ans(int i, int X, int Y) {
  if (X <= 0 && Y <= 0) return 0;
  if (i == N) return 500;
  if (X < 0) X = 0;
  if (Y < 0) Y = 0;
  if (memo[i][X][Y] != -1) return memo[i][X][Y];
  int r = min(
    1+ans(i+1, X-xs[i], Y-ys[i]),
    ans(i+1, X, Y)
  );
  return memo[i][X][Y] = r;

}
int main() {

  memset(memo, -1, sizeof(memo));

  cin >> N >> X >> Y;
  for (int i=0; i<N; i++) {
    cin >> xs[i] >> ys[i];
  }

  int r = ans(0, X, Y);

  if (r >= 500) r = -1;

  cout << r << endl;

  return 0;
}
