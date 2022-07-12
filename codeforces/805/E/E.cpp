#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

constexpr int MAX_N = 200009;
int N;
vector<int> neighbours[MAX_N];
int degree[MAX_N];

bool is_bipartite() {
  int n = N;

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

bool ans() {
    for (int i=0; i<N; i++) {
      if (neighbours[i].size() > 2) {
        return false;
      }
    }
    return is_bipartite();
}

i32 main() {

  int T;
  cin >> T;
  while (T --> 0) {
    cin >> N;
    for (int i=0; i<N; i++) {
      neighbours[i].clear();
      degree[i] = 0;
    }
    for (int i=0; i<N; i++) {
      int a, b;
      cin >> a >> b;
      a--; b--;
      neighbours[a].push_back(b);
      neighbours[b].push_back(a);
    }
    if (ans()) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }

  return 0;
}

