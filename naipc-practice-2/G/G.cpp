#include <cstdio>
#include <map>
#include <vector>
#include <utility>
#include <cstdlib>

using namespace std;

#define max_N 1005

int next[MAX_N];
int dfs_col[MAX_N];
int dfs_num[MAX_N];

void dfs(int v, int num, int col) {
  if (dfs_col[v] != -1) {
    return;
  }
  dfs_col[v] = col;
  dfs_num[v] = num;
  dfs(next[v], num + 1, col);
}

int main() {

  int N, K;

  scanf("%d %d\n", &N, &K);

  for (int v = 1; v <= K; v++) {
    dfs_num[v] = -1;
    dfs_col[v] = -1;
    scanf("%d", &next[v]);
  }



  return 0;
}
