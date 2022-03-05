#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int N;
vector<pair<int, int>> points;
map<pair<int, int>, int> idx_of;
map<int, int> last_x_of_y;
vector<tuple<int,int,int>> edges;

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

void add_edge(int X, int Y, int x, int y) {
  auto dx = X-x;
  auto dy = Y-y;
  edges.push_back({dx*dx + dy*dy, idx_of[{X, Y}], idx_of[{x, y}]});
}

int kruskal(int V, vector<tuple<int,int,int>>& edges) {
  auto uf = UF(V);
  int ret = 0;
  sort(edges.begin(), edges.end());

  for (auto t : edges) {
    auto [w, u, v] = t;
    if (uf.sameSet(u, v)) continue;
    uf.join(u, v);
    ret += w;
  }

  return ret;

}

i32 main() {

  ios_base::sync_with_stdio(false); cin.tie(NULL);

  cin >> N;
  for (int i=0; i<N; i++) {
    int x, y;
    cin >> x >> y;
    points.push_back({x, y});
    idx_of[{x, y}] = i;
  }

  sort(points.begin(), points.end());

  for (auto [x, y] : points) {
    for (auto p : last_x_of_y) {
      auto Y = p.first;
      auto X = p.second;
      add_edge(x, y, X, Y);
    }
    last_x_of_y[y] = x;
  }

  cout << kruskal(N, edges) << endl;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS