#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>
#include <unordered_map>
#include <cassert>

using namespace std;
#define int long long
#define i32 int32_t
#define i64 int64_t

int N, M, Q;

vector<pair<int, int>> neighbours[100009];
bool visited[100009];
int depth[100009];
int root_of[100009];
bool has_cycle[100009];

void dfs(int u, int root) {
  visited[u] = true;
  root_of[u] = root;
  for (auto& [v, w] : neighbours[u]) {
    if (visited[v] && (depth[v] != (depth[u] + w))) {
      has_cycle[root] = true;
    }
    depth[v] = depth[u] + w;
    
    if (!visited[v]) dfs(v, root);
  }
}
i32 main() {

  memset(visited, 0, sizeof(visited));
  memset(has_cycle, 0, sizeof(has_cycle));

  cin.tie(0);

  cin >> N >> M >> Q;
  
  for (int i=0; i<M; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    neighbours[a].push_back({b, c});
    neighbours[b].push_back({a, -c});
  }

  for (int i=1; i<=N; i++) {
    if (visited[i]) continue;
    // cout << "visit " << i << endl;
    depth[i] = 0;
    dfs(i, i);
  }

  for (int i=0; i<Q; i++) {
    int X, Y;
    cin >> X >> Y;
    // cout << "X=" << X << "Y=" << Y << endl;
    if (root_of[X] != root_of[Y]) {
      cout << "nan" << endl;
      continue;
    }
    int root = root_of[X];
    if (has_cycle[root]) {
      cout << "inf" << endl;
      continue;
    }
    cout << (depth[Y] - depth[X]) << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS