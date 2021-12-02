#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> children[200009];
int subtree_size[200009];
int ans[200009];
int subtree_sum[200009];

void dfs0(int u, int parent) {
  for (auto v : children[u]) {
    if (v == parent) continue;
    dfs0(v, u);
    cout << u << "->" << v << endl;
    subtree_size[u] += subtree_size[v];
  }
}

int main() {

  cin >> N;
  for (int i=0; i<N; i++) subtree_size[i] = 1;

  for (int i=0; i<N-1; i++) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    children[u].push_back(v);
    children[v].push_back(u);
  }

  dfs0(0, 0);

  for (int i=0; i<N; i++) cout << subtree_size[i] << " ";
  cout << endl;

  return 0;
}
