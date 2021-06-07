#include <bits/stdc++.h>
using namespace std;

int N, M;
int reachable[2009][2009];
vector<int> neighbours[2009];

void dfs(int daddy, int u) {
  if (reachable[daddy][u]) return;
  reachable[daddy][u] = true;
  for (int v : neighbours[u]) {
    dfs(daddy, v);
  }
}

int main() {

  memset(reachable, 0, sizeof(reachable));

  cin >> N >> M;
  for (int i=0; i<M; i++) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    neighbours[u].push_back(v);
  }

  for (int i=0; i<N; i++) {
    dfs(i, i);
  }

  int ret = 0;
  for (int i=0; i<N; i++) {
    for (int j=0; j<N; j++) {
      if (reachable[i][j]) {
        ret++;
      }
    }
  }

  cout << ret << endl;

  return 0;
}
