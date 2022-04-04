#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int N, M;

vector<int> neighbours[200009];
int visited[200009];
bool ok[200009];

void dfs(int daddy, int u) {
  if (visited[u]) return;
  visited[u] = 1;
  if (neighbours[u].size() != 2) {
    ok[daddy] = 0;
  }
  for (auto v : neighbours[u]) {
    dfs(daddy, v);
  }
}

i32 main() {

  memset(visited, 0, sizeof(visited));
  memset(ok, 1, sizeof(ok));

  cin >> N >> M;
  while (M --> 0) {
    int u, v;
    cin >> u >> v;
    neighbours[u].push_back(v);
    neighbours[v].push_back(u);
  }

  int ret = 0;
  for (int i=1; i<=N; i++) {
    if (!visited[i]) {
      dfs(i, i);
      if (ok[i]) ret++;
    }
  }

  cout << ret << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS