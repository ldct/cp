#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

int N, M;

vector<int> neighbours[200009];
bool visited[200009];
bool has_cycle;

void dfs(int u, int parent) {
  for (auto v : neighbours[u]) {
    if (v == parent) continue;
    if (visited[v]) {
      has_cycle = true;
    } else {
      visited[v] = true;
      dfs(v, u);
    }
  }
}

bool ans() {
  for (int i=0; i<N; i++) {
    if (neighbours[i].size() > 2) return false;
  }
  has_cycle = false;

  for (int i=0; i<N; i++) {
    if (!visited[i]) dfs(i, i);
  }

  return !has_cycle;
}

i32 main() {

  memset(visited, 0, sizeof(visited));

  cin >> N >> M;

  for (int i=0; i<M; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    neighbours[a].push_back(b);
    neighbours[b].push_back(a);
  }

  if (ans()) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

}
