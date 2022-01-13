#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

int N;

vector<int> neighbours[200009];
int height[200009];
int height2[200009];
int ans[200009];

void chmax(int& x, int& y, int val) {
  if (val >= x) {
    y = x;
    x = val;
  } else {
    y = max(y, val);
  }
}

int dfs(int u, int parent) {

  height[u] = 0;
  height2[u] = 0;

  for (auto v : neighbours[u]) {
    if (v == parent) continue;
    chmax(height[u], height2[u], 1 + dfs(v, u));
  }

  return height[u];
}

void walk(int u, int parent) {

  ans[u] = height[u];

  for (auto v : neighbours[u]) {
    if (v == parent) continue;

    /*
    u
    |
    v
    */

    vector<int> save = { height[u], height2[u], height[v], height2[v]};
    // cout << u << " is now the root and has height " << height[u] << " " << height2[u] << endl;

    // remove v as a child of u
    if (height[u] == 1 + height[v]) {
      height[u] = height2[u];
      height2[u] = 0;
    }



    // add u as a child of v
    chmax(height[v], height2[v], 1 + height[u]);

    // cout << v << " is now the root and has height " << height[v] << " " << height2[v] << endl;

    walk(v, u);

    // undo
    height[u] = save[0]; height2[u] = save[1]; height[v] = save[2]; height2[v] = save[3];
  }
}



i32 main() {

  cin >> N;
  for (int i=0; i<N-1; i++) {
    int a, b;
    cin >> a >> b;
    neighbours[a].push_back(b);
    neighbours[b].push_back(a);
  }

  dfs(1, 1);
  walk(1, 1);

  for (int i=1; i<=N; i++) {
    cout << ans[i] << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS