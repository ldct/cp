#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

struct UF {
  vector<int> e;
  UF(int n) : e(n, -1) {}
  bool sameSet(int a, int b) { return find(a) == find(b); }
  int size(int x) { return -e[find(x)]; }
  int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
  bool join(int a, int b) {
    a = find(a), b = find(b);
    if (a == b) return false;
    if (e[a] > e[b]) swap(a, b);
    e[a] += e[b]; e[b] = a;
    return true;
  }
};

int N, M;
vector<pair<int, pair<int, int>>> edges;

bool ok(int mask) {
  auto uf = UF(N);

  for (auto edge : edges) {
    if (mask == (mask | edge.first)) uf.join(edge.second.first, edge.second.second);
  }

  return uf.size(0) == N;
}

int turn_off(int n, int k) {
  return (n & ~(1LL << k));
}

i32 main() {

  int T;

  cin >> T;

  while (T --> 0) {
    edges.clear();
    cin >> N >> M;
    for (int i=0; i<M; i++) {
      int u, v, w;
      cin >> u >> v >> w;
      u--; v--;
      edges.push_back({w, {u, v}});
    }

    int ret = INT_MAX;
    for (int i=30; i!=-1; i--) {
      int test = turn_off(ret, i);
      if (ok(test)) ret = test;
    }
    cout << ret << endl;
  }

  return 0;
}
