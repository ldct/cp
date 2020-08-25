#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

constexpr size_t MAX_N = 300009;

int N;
vector<int> neighbours[MAX_N];
int max_depth;
int depth_of[MAX_N];
bool is_diameter_leaf[MAX_N];
int subtree_max_depth[MAX_N];
vector<int> diameter;

void mark_diameter(int u, int parent, int target) {
  assert(subtree_max_depth[u] == target);
  diameter.push_back(u);
  for (const auto& v : neighbours[u]) {
    if (v == parent) continue;
    if (subtree_max_depth[v] == target) {
      mark_diameter(v, u, target);
      return;
    }
  }
}

int dfs(int u, int parent, int depth) {
  depth_of[u] = depth;
  max_depth = max(max_depth, depth);
  int this_subtree_max_depth = depth;
  for (const auto& v : neighbours[u]) {
    if (v == parent) continue;
    this_subtree_max_depth = max(this_subtree_max_depth, dfs(v, u, depth+1));
  }
  subtree_max_depth[u] = this_subtree_max_depth;
  return this_subtree_max_depth;
}

void dfs2(int u, int p1, int p2, int depth, int target) {
  if (depth == target) {
    // cout << "marking " << u << endl;
    is_diameter_leaf[u] = true;
  }
  for (const auto& v : neighbours[u]) {
    if (v == p1) continue;
    if (v == p2) continue;
    dfs2(v, u, u, depth+1, target);
  }
}

int main() {
  
  cin >> N;

  for (int i=0; i<N; i++) {
    is_diameter_leaf[i] = false;
  }

  for (int i=0; i<N-1; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    neighbours[a].push_back(b);
    neighbours[b].push_back(a);
  }

  max_depth = -1;
  dfs(0, 0, 0);

  int new_root;
  for (int i=0; i<N; i++) {
    if (depth_of[i] == max_depth) {
      new_root = i;
    }
  }

  // cout << "new_root=" << new_root << endl;

  max_depth = -1;
  dfs(new_root, new_root, 0);

  mark_diameter(new_root, new_root, max_depth);

  // cout << diameter << endl;

  is_diameter_leaf[diameter[0]] = is_diameter_leaf[diameter[diameter.size()-1]] = true;

  for (int i=0; i<diameter.size(); i++) {
    const auto u = diameter[i];
    int md = min(depth_of[u], (int)diameter.size()-1-depth_of[u]);

    if (md > 0) {
      dfs2(u, diameter[i-1], diameter[i+1], 0, md);
    }
  }

  for (int i=0; i<N; i++) {
    if (is_diameter_leaf[i]) {
      cout << max_depth+1 << endl;
    } else {
      cout << max_depth << endl;
    }
  }

  return 0;
}
