#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 100009;
int N, A, B, DA, DB;

vector<int> neighbours[MAX_N];

int max_depth;
int depth_of[MAX_N];
int subtree_max_depth[MAX_N];

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

void ans() {
  if (!(DB > 2*DA)) {
    cout << "Alice" << endl;
    return;
  }

  max_depth = -1;
  dfs(A, A, 0);

  if (depth_of[B] <= DA) {
    cout << "Alice" << endl;
    return;
  }

  int new_root;
  for (int i=0; i<N; i++) {
    if (depth_of[i] == max_depth) {
      new_root = i;
    }
  }

  max_depth = -1;
  dfs(new_root, new_root, 0);

  if (!(max_depth > 2*DA)) {
    cout << "Alice" << endl;
    return;
  }

  cout << "Bob" << endl;
}

int main() {
  
  int T;
  cin >> T;

  while (T --> 0) {
    cin >> N >> A >> B >> DA >> DB;
    A--; B--;

    for (int i=0; i<N; i++) {
      neighbours[i].clear();
    }

    for (int i=0; i<N-1; i++) {
      int a, b;
      cin >> a >> b;
      a--; b--;
      neighbours[a].push_back(b);
      neighbours[b].push_back(a);
    }
    ans();
  }
    
  return 0;
}
