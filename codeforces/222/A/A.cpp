#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

int N, M, K;
char grid[509][509];

int to_visit = 0;

void dfs(int i, int j) {
  if (to_visit == 0) return;
  if (!(0 <= i && i < N)) return;
  if (!(0 <= j && j < M)) return;
  if (grid[i][j] != ' ') return;

  grid[i][j] = '.';
  to_visit--;
  dfs(i, j+1);
  dfs(i, j-1);
  dfs(i+1, j);
  dfs(i-1, j);
}

i32 main() {

  int num_empty = 0;

  cin >> N >> M >> K;
  for (int i=0; i<N; i++) for (int j=0; j<M; j++) {
    cin >> grid[i][j];
    if (grid[i][j] == '.') {
      grid[i][j] = ' ';
      num_empty++;
    }
  }

  to_visit = num_empty - K;

  for (int i=0; i<N; i++) for (int j=0; j<M; j++) dfs(i, j);

  for (int i=0; i<N; i++) {
    for (int j=0; j<M; j++) {
      if (grid[i][j] == ' ') grid[i][j] = 'X';
      cout << grid[i][j];
    }
    cout << endl;
  }


  return 0;
}
