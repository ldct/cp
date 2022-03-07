#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

using namespace std;

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

int N, C;
vector<pair<int, int>> points;
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

void add_edge(int i, int j) {
  auto [X, Y] = points[i];
  auto [x, y] = points[j];
  auto dx = X-x;
  auto dy = Y-y;
  auto w = dx*dx + dy*dy;
  if (w < C) return;
  vector<int> r = {X, Y, x, y};
  edges.push_back({w, i, j});
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

  for (int i=0; i<V; i++) {
    if (!uf.sameSet(0, i)) return -1;
  }

  return ret;

}

i32 main() {
  int x, y;

  freopen("irrigation.in", "r", stdin);
  freopen("irrigation.out", "w", stdout);

  scanf("%lld %lld", &N, &C);

  for (int i = 0; i < N; i++) {
    scanf("%lld %lld", &x, &y);
    points.push_back({x, y});
  }

  for (int i=0; i<points.size(); i++) {
    for (int j=i; j<points.size(); j++) {
      add_edge(i, j);
    }
  }

  cout << kruskal(N, edges) << endl;

  return 0;
}
