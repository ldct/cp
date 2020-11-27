#include <bits/stdc++.h>
using namespace std;

bool is_bipartite(vector<vector<int>>& neighbours) {
  int n = neighbours.size();

  vector<int> side(n, -1);
  bool is_bipartite = true;
  queue<int> q;
  for (int st = 0; st < n; ++st) {
    if (side[st] == -1) {
      q.push(st);
      side[st] = 0;
      while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int u : neighbours[v]) {
          if (side[u] == -1) {
            side[u] = side[v] ^ 1;
            q.push(u);
          } else {
            is_bipartite &= side[u] != side[v];
          }
        }
      }
    }
  }
  return is_bipartite;
}

int N;
int A[509][509];

bool ok(int pv) {
  vector<vector<int>> neighbours(N);
  for (int i=0; i<N; i++) {
    for (int j=0; j<N; j++) {
      if (i == j) continue;
      if (A[i][j] < pv) {
        neighbours[i].push_back(j);
      }
    }
  }
  return is_bipartite(neighbours);
}

int main() {

  cin >> N;

  for (int i=0; i<N; i++) {
    for (int j=0; j<N; j++) {
      cin >> A[i][j];
    }
  }

  int low = 0;
  int high = 1000000001;

  assert(ok(low));
  assert(!ok(high));

  while (high - low > 2) {
    int mid = (low + high) / 2;
    if (ok(mid)) {
      low = mid;
    } else {
      high = mid;
    }
  }

  for (int i=low;; i++) {
    if (!ok(i)) {
      cout << i-1 << endl;
      return 0;
    }
  }

  return 0;
}
