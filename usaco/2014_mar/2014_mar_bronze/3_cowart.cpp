#include <cstdio>
#include <utility>
#include <cstring>
#define MAX_N 101
#define DFS_WHITE 0
#define DFS_BLACK 1

using namespace std;

int N;
int RGB[MAX_N][MAX_N];
int RB[MAX_N][MAX_N];
int dfs_colour[MAX_N][MAX_N];

void dfs(int i, int j, int arr[MAX_N][MAX_N]) {
  dfs_colour[i][j] = DFS_BLACK;
  int my_rgb = arr[i][j];
  if (i > 0) {
    if (dfs_colour[i-1][j] == DFS_WHITE && my_rgb == arr[i-1][j]) {
      dfs(i-1, j, arr);
    }
  }
  if (j > 0) {
    if (dfs_colour[i][j-1] == DFS_WHITE && my_rgb == arr[i][j-1]) {
      dfs(i, j-1, arr);
    }
  }
  if (i < N-1) {
    if (dfs_colour[i+1][j] == DFS_WHITE && my_rgb == arr[i+1][j]) {
      dfs(i+1, j, arr);
    }
  }
  if (j < N-1) {
    if (dfs_colour[i][j+1] == DFS_WHITE && my_rgb == arr[i][j+1]) {
      dfs(i, j+1, arr);
    }
  }
  return;
}

pair<int,int> find_unvisited() {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (dfs_colour[i][j] == 0) {
        return make_pair(i,j);
      }
    }
  }
  return make_pair(-1,-1);
}

int main() {

  freopen("cowart.in", "r", stdin);
  freopen("cowart.out", "w", stdout);

  int i,j;
  int num_rgb = 0;
  int num_rb = 0;

  scanf("%d", &N);
  for (i = 0; i < N; i++) {
    for (j = 0; j < N; j++) {
      char c;
      scanf(" %c", &c);
      if (c == 'R') RGB[i][j] = 0, RB[i][j] = 0;
      if (c == 'G') RGB[i][j] = 1, RB[i][j] = 0;
      if (c == 'B') RGB[i][j] = 2, RB[i][j] = 1;
    }
  }

  pair<int,int> next = make_pair(0,0);
  while (next.first != -1 && next.second != -1) {
    num_rgb++;
    dfs(next.first, next.second, RGB);
    next = find_unvisited();
  }

  memset(dfs_colour, DFS_WHITE, sizeof dfs_colour);

  next = make_pair(0,0);
  while (next.first != -1 && next.second != -1) {
    num_rb++;
    dfs(next.first, next.second, RB);
    next = find_unvisited();
  }

  printf("%d %d\n", num_rgb, num_rb);

  return 0;
}
