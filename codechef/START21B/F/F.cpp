#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

int N;
string colour;
vector<int> neighbours[200009];

vector<int> contracted_children[200009];

int nn_R[200009];
int nn_G[200009];
int nn_B[200009];

bool ok;

void dfs_cc(int u, int parent, int daddy) {
  // form the contracted graph
  if (colour[u] != colour[daddy]) {
    contracted_children[daddy].push_back(u);
    for (auto v : neighbours[u]) {
      if (v == parent) continue;
      dfs_cc(v, u, u);
    }
  } else {
    for (auto v : neighbours[u]) {
      if (v == parent) continue;
      dfs_cc(v, u, daddy);
    }
  }
}

void update(int u, int v) {
  if (colour[u] == 'R') nn_R[v]++;
  if (colour[u] == 'G') nn_G[v]++;
  if (colour[u] == 'B') nn_B[v]++;
}

void dfs_blue(int u, int parent) {
  // check for blue -> blue edges
  if (u != parent) {
    if (colour[u] == colour[parent] && colour[u] == 'B') {
      ok = false;
    }
  }

  for (auto v : neighbours[u]) {
    if (v == parent) continue;
    dfs_blue(v, u);
  }
}

void dfs_nn(int u, int parent) {
  // calculate number of neighbours for each
  if (u != parent) {
    update(u, parent);
    update(parent, u);
  }

  for (auto v : contracted_children[u]) {
    if (v == parent) continue;
    dfs_nn(v, u);
  }
}

void check(int u) {
  if (colour[u] == 'B') return;
  if (nn_B[u] > 1) ok = false;
}

void dfs(int u, int parent) {
  check(u);
  for (auto v : contracted_children[u]) {
    if (v == parent) continue;
    dfs(v, u);
  }
}

i32 main() {

  int T;
  cin >> T;
  while (T --> 0) {
    ok = true;
    cin >> N;
    for (int i=0; i<N; i++) {
      neighbours[i].clear();
      contracted_children[i].clear();
      nn_R[i] = 0;
      nn_G[i] = 0;
      nn_B[i] = 0;
    }
    cin >> colour;
    for (int i=0; i<N-1; i++) {
      int u, v;
      cin >> u >> v;
      u--; v--;
      neighbours[u].push_back(v);
      neighbours[v].push_back(u);
    }
    dfs_blue(0, 0);
    dfs_cc(0, 0, 0);
    dfs_nn(0, 0);
    dfs(0, 0);

    if (ok) {
      cout << "Yes" << endl;
    } else {
      cout << "No" << endl;
    }
  }

  return 0;
}
