#include <bits/stdc++.h>
using namespace std;

int T;

vector<int> neighbours[100009];
int _sss[100009];

int target;
int num_good;

int dfs(vector<int>& A, int parent, int u) {
  int ret = A[u];
  for (auto v : neighbours[u]) {
    if (v == parent) continue;
    int r = dfs(A, u, v);
    if (r == target) {
      r = 0;
      num_good += 1;
    }
    ret ^= r;
  }
  return ret;
}

int subtree_sum(vector<int>& A, int parent, int u) {
  int ret = A[u];
  for (auto v : neighbours[u]) {
    if (v == parent) continue;
    ret ^= subtree_sum(A, u, v);
  }
  return _sss[u] = ret;
}



string ans(int N, int K, vector<int>& A, vector<pair<int, int>>& edges) {
  for (int i=0; i<N; i++) {
    neighbours[i].clear();
    _sss[i] = -1;
  }

  for (auto [u, v] : edges) {
    neighbours[u].push_back(v);
    neighbours[v].push_back(u);
  }

  int TOTAL = 0;
  for (auto a : A) TOTAL ^= a;

  int check = subtree_sum(A, 0, 0);

  assert(check == TOTAL);

  for (int i=0; i<N; i++) {
    assert(_sss[i] >= 0);
  }

  if (TOTAL == 0) {
    for (int i=0; i<N; i++) {
      if (_sss[i] == 0) return "YES";
    }
    return "NO";
  }

  if (K == 2) return "NO";

  num_good = 0;
  target = TOTAL;

  dfs(A, 0, 0);

  if (num_good >= 2) return "YES";

  return "NO";
}

int main() {

  cin >> T;
  while (T --> 0) {
    int N, K;
    cin >> N >> K;
    vector<int> A;
    for (int i=0; i<N; i++) {
      int a;
      cin >> a;
      A.push_back(a);
    }
    vector<pair<int, int>> edges;
    for (int i=0; i<N-1; i++) {
      int u, v;
      cin >> u >> v;
      u--; v--;
      edges.push_back({u, v});
    }
    cout << ans(N, K, A, edges) << endl;
  }

  return 0;
}
