#include <bits/stdc++.h>
using namespace std;

int T;

vector<int> neighbours[200009];
int colour[200009];

void dfs(int u, int parent, int c_set) {
  colour[u] = c_set;
  for (auto v : neighbours[u]) {
    if (v == parent) continue;
    dfs(v, u, 1-c_set);
  }
}

int main() {

  cin >> T;
  while (T-->0) {
    int N;
    cin >> N;
    for (int i=0; i<N; i++) neighbours[i].clear();
    for (int i=0; i<N-1; i++) {
      int u, v;
      cin >> u >> v;
      u--; v--;
      neighbours[u].push_back(v);
      neighbours[v].push_back(u);
    }
    dfs(0, 0, 0);
    for (int i=0; i<N; i++) {
      cout << (i+1) << " " << colour[i] << endl;
    }
    cout << endl;
  }

  return 0;
}
