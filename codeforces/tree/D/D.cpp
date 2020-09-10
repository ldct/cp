#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 300009;

int N, M, Q;
map<int, int> neighbours[MAX_N];
int depth[MAX_N];
int ancestor2[MAX_N][21];
int weight2[MAX_N][21];

void dfs(int u, int parent, int curr_depth) {
  depth[u] = curr_depth;
  ancestor2[u][0] = parent;
  for (const auto& p : neighbours[u]) {
    int v = p.first;
    int w = p.second;
    if (v == parent) continue;
    weight2[v][0] = w;
    dfs(v, u, curr_depth+1);
  }
}

pair<int, int> ancestor(int u, int n) {
  int w = INT_MAX;
  for (int e = 21; e >= 0; e--) {
    if (u == -1) return {u, w};
    if ((1 << e) <= n) {
      n -= (1 << e);
      w = min(w, weight2[u][e]);
      u = ancestor2[u][e];
    }
  }
  assert(n == 0);
  return {u, w};
} 

int lca(int u, int v) {
  if (depth[u] > depth[v]) return lca(v, u);
  assert(depth[u] <= depth[v]);
  v = ancestor(v, depth[v] - depth[u]).first;

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

int query(int a, int b) {
  int l = lca(a, b);
  int aw = ancestor(a, depth[a] - depth[l]).second;
  int bw = ancestor(b, depth[b] - depth[l]).second;
  // cout << "a=" << a << "b=" << b << "l=" << l << endl;
  // cout << "aw=" << aw << endl;
  // cout << "bw=" << bw << endl;
  return min(aw, bw);
}

int main() {
  
  cin >> N >> M;
  assert(M == N-1);

  for (int i=0; i<N-1; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    u--; v--;
    neighbours[u][v] = w;
    neighbours[v][u] = w;
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
        weight2[u][e] = min(weight2[u][e-1], weight2[ancestor2[u][e-1]][e-1]);
      } else {
        ancestor2[u][e] = -1;
      }
    }
  }

  cin >> Q;

  while (Q --> 0) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    cout << query(a, b) << endl;
  }
    
  return 0;
}
