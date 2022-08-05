#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>
#include <queue>

using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int N, M;
vector<int> neighbours[200009];
bool visited[200009];

void bfs(int s) {

  queue<int> q;
  vector<bool> used(N+1);
  vector<int> d(N+1), p(N+1);

  q.push(s);
  used[s] = true;
  p[s] = -1;
  while (!q.empty()) {
      int v = q.front();
      q.pop();
      for (int u : neighbours[v]) {
          if (!used[u]) {
            cout << u << " " << v << endl;
              used[u] = true;
              q.push(u);
              d[u] = d[v] + 1;
              p[u] = v;
          }
      }
}

}
void dfs(int u) {
  visited[u] = true;
  for (auto v : neighbours[u]) {
    if (visited[v]) continue;
    cout << u << " " << v << endl;
    dfs(v);
  }
}

i32 main() {

  cin >> N >> M;
  for (int i=0; i<M; i++) {
    int u, v;
    cin >> u >> v;
    neighbours[u].push_back(v);
    neighbours[v].push_back(u);
  }
  dfs(1);
  bfs(1);

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS