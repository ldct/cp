#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

int N;
char grid[59][59];

i32 memo_ie[59][59][59][59];
i32 memo_ans[59][59][59][59];

bool x_is_empty(int x1, int x2, int y1, int y2) {
  if (memo_ie[x1][x2][y1][y2] != -1) return (memo_ie[x1][x2][y1][y2] == 1);
  for (int x=x1; x<x2; x++) for (int y=y1; y<y2; y++) if (grid[x][y] == '#') {
    memo_ie[x1][x2][y1][y2] = 0;
    return false;
  }
  memo_ie[x1][x2][y1][y2] = 1;
  return true;
}

i32 ans(int x1, int x2, int y1, int y2) {
  if (memo_ans[x1][x2][y1][y2] != -1) return memo_ans[x1][x2][y1][y2];
  i32 ret = INT_MAX;
  if (x2 - x1 == y2 - y1) ret = x2 - x1;
  if (x_is_empty(x1, x2, y1, y2)) return memo_ans[x1][x2][y1][y2] = 0;

  for (int x=x1+1; x<x2; x++) {
    ret = min(ret,
        ans(x1, x, y1, y2) + ans(x, x2, y1, y2)
    );
  }


  for (int y=y1+1; y<y2; y++) {
    ret = min(ret,
        ans(x1, x2, y1, y) + ans(x1, x2, y, y2)
    );
  }
  return memo_ans[x1][x2][y1][y2] = ret;
}


i32 main() {

  cin >> N;

  memset(memo_ie, -1, sizeof(memo_ie));
  memset(memo_ans, -1, sizeof(memo_ans));

  for (int i=0; i<N; i++) for (int j=0; j<N; j++) {
    char c;
    cin >> c;
    assert(c == '#' || c == '.');
    grid[i][j] = c;
  }

  cout << ans(0, N, 0, N) << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS