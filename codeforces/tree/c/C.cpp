#include <bits/stdc++.h>
using namespace std;

/*
for exp : 1 -> 20
  for node
    if node.lift[e-1]
      node.lift[e] = node.lift[e-1].lift[e-1]
*/

constexpr size_t MAX_N = 300009;

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

int query(int a, int b, int c) {
  int l = lca(a, b);

  int up = min(depth[a] - depth[l], c);

  c -= up;

  if (c == 0) {
    return ancestor(a, up);
  }

  int up2 = depth[b] - depth[l] - c;
  if (up2 < 0) up2 = 0;

  return ancestor(b, up2);
}

int main() {
  
  cin >> N;
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

  cin >> Q;
  while (Q --> 0) {
    int a, b, c;
    cin >> a >> b >> c;
    a--; b--;
    cout << query(a, b, c) + 1 << endl;
  }
    
  return 0;
}
