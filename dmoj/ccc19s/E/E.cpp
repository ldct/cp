#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int N, K;
int triangle[3009][3009];
int maxSqLg_memo[3009][3009][13];
int maxTriLg_memo[3009][3009][13];

int max3(int a, int b, int c) { return max(max(a, b), c); }
int max4(int a, int b, int c, int d) { return max(max(a, b), max(c, d)); }

int maxSqLg(int x, int y, int lg) {
  if (lg == 0) return triangle[x][y];
  if (maxSqLg_memo[x][y][lg] != -1) return maxSqLg_memo[x][y][lg];
  auto d = 1 << (lg-1);
  return maxSqLg_memo[x][y][lg] = max4(
      maxSqLg(x, y, lg-1),
      maxSqLg(x+d, y, lg-1),
      maxSqLg(x, y+d, lg-1),
      maxSqLg(x+d, y+d, lg-1)
  );
}

int maxTriLg(int x, int y, int lg) {
  if (lg == 0) return triangle[x][y];
  if (maxTriLg_memo[x][y][lg] != -1) return maxTriLg_memo[x][y][lg];
  auto d = 1 << (lg-1);
  return maxTriLg_memo[x][y][lg] = max3(
      maxTriLg(x, y, lg-1),
      maxSqLg(x+d, y, lg-1),
      maxTriLg(x+d, y+d, lg-1)
  );
}

int maxSq(int x, int y, int D) {
  if (D == 1) return triangle[x][y];
  assert(D > 1);
  int i = 0;
  while ((1 << i) <= D) i++;
  i--;
  assert((1 << i) <= D);
  int d = D - (1 << i);
  if (d == 0) return maxSqLg(x, y, i);
  return max4(
      maxSqLg(x, y, i),
      maxSqLg(x + d, y, i),
      maxSqLg(x, y + d, i),
      maxSqLg(x + d, y + d, i)
  );
}

int maxSqBL(int x, int y, int D) {
  return maxSq(x + D - 1, y, D);
}

int maxTri(int x, int y, int D) {
  if (D == 1) return triangle[x][y];
  assert(D > 1);
  int i = 0;
  while ((1 << i) <= D) i++;
  i--;
  assert((1 << i) <= D);
  int d = D - (1 << i);
  if (d == 0) return maxTriLg(x, y, i);
  return max3(
      maxTriLg(x, y, i),
      maxSqBL(x, y, d),
      maxTriLg(x + d, y, i)
  );
}


i32 main() {

  memset(maxSqLg_memo, -1, sizeof(maxSqLg_memo));
  memset(maxTriLg_memo, -1, sizeof(maxTriLg_memo));

  cin >> N >> K;
  for (int i=1; i<=N; i++) {
    for (int j=0; j<i; j++) {
      cin >> triangle[i-1][j];
    }
  }

  for (int i=0; i<N; i++) {
    for (int j=0; j<N; j++) {
      // cout << triangle[i][j] << " ";
    }
    // cout << endl;
  }

  // cout << maxTriLg(0, 0, 1) << endl;

  int ret = 0;
  for (int x=0; x<=N-K; x++) {
    for (int y=0; y<=x; y++) {
      // cout << x << " " << y << " " << maxTri(x, y, K) << endl;
      ret += maxTri(x, y, K);
    }
  }

  cout << ret << endl;
  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS