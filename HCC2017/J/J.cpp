#include <bits/stdc++.h>
using namespace std;

int N;
vector<pair<int, int>> neighbours[109];

int dfs(int u, int parent) {
  int ret = 0;
  for (auto p : neighbours[u]) {
    int v = p.first;
    int w = p.second;
    if (v == parent) continue;
    ret = max(ret,
      w + dfs(v, u)
    );
  }
  return ret;
}

int main() {

  cin >> N;
  for (int i=0; i<N-1; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    neighbours[u].push_back({v, w});
    neighbours[v].push_back({u, w});
  }
  cout << dfs(0, -1) << endl;

  return 0;
}
