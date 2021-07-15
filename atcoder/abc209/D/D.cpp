#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 100009;

int N, Q;
vector<int> neighbours[MAX_N];
int depth[MAX_N];
int ancestor2[MAX_N][21];

void dfs(int u, int parent, int curr_depth) {
  depth[u] = curr_depth;
  ancestor2[u][0] = parent;
  for (const auto& v : neighbours[u]) {
    if (v == parent) continue;
    dfs(v, u, curr_depth+1);
  }
}

int ancestor(int u, int n) {
  for (int e = 21; e >= 0; e--) {
    if (u == -1) return u;
    if ((1 << e) <= n) {
      n -= (1 << e);
      u = ancestor2[u][e];
    }
  }
  assert(n == 0);
  return u;
}

int lca(int u, int v) {
  if (depth[u] > depth[v]) return lca(v, u);
  assert(depth[u] <= depth[v]);
  v = ancestor(v, depth[v] - depth[u]);

  for (int e=20; e>=0; e--) {
    if (u == v) return u;
    if (ancestor2[u][e] != ancestor2[v][e]) {
      u = ancestor2[u][e];
      v = ancestor2[v][e];
    }
  }
  if (u == v) return u;
  assert(ancestor2[u][0] == ancestor2[v][0]);
  return ancestor2[u][0];
}

string query(int a, int b) {
  int l = lca(a, b);
  int dist = 0;
  if (l == a) {
    dist = depth[b] - depth[a];
  } else if (l == b) {
    dist = depth[a] - depth[b];
  } else {
    dist = depth[a] + depth[b] - 2*depth[l];
  }

  // cout << "lca(" << a << "," << b << ")=" << l << endl;
  // cout << "dist(" << a << "," << b << ")=" << dist << endl;

  assert(dist >= 0);

  if (dist % 2 == 0) {
    return "Town";
  } else {
    return "Road";
  }
}

int main() {

  cin >> N >> Q;
  for (int i=0; i<N-1; i++) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    neighbours[u].push_back(v);
    neighbours[v].push_back(u);
  }

  dfs(0, -1, 0);

  for (int e=1; e <= 20; e++) {
    ancestor2[0][e] = -1;
  }

  // TAG:binary lifting
  for (int e=1; e <= 20; e++) {
    for (int u=0; u<N; u++) {
      if (ancestor2[u][e-1] != -1) {
        ancestor2[u][e] = ancestor2[ancestor2[u][e-1]][e-1];
      } else {
        ancestor2[u][e] = -1;
      }
    }
  }

  // for (int i=0; i<N; i++) {
  //   cout << depth[i] << endl;
  // }
  // return 0;

  while (Q --> 0) {
    int a, b;
    cin >> a >> b;;
    a--; b--;
    cout << query(a, b) << endl;
  }

  return 0;
}
