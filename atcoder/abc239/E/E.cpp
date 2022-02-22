#include <bits/stdc++.h>

using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

int N, Q;

int X[100009];
int parent[100009];
vector<int> neighbours[100009];

map<int, int> queries_at_node[200009];
vector<pair<int, int>> queries;

vector<int> subtree_vals[100009];

void dfs0(int p, int u) {
  parent[u] = p;
  for (auto v : neighbours[u]) {
    if (v == p) continue;
    dfs0(u, v);
  }
}

void dfs1(int p, int u) {
  for (auto v : neighbours[u]) {
    if (v == p) continue;
    dfs1(u, v);
  }


  for (auto v : neighbours[u]) {
    if (v == p) continue;
    // cout << "merge subtree_vals[" << v << "]=" << subtree_vals[v].size() << " into subtree_vals[" << u << "]" << endl;
    // merge subtree_vals[v] into subtree_vals[u]
    for (auto x : subtree_vals[v]) {
      subtree_vals[u].push_back(x);
    }
  }

  subtree_vals[u].push_back(X[u]);
  sort(subtree_vals[u].begin(), subtree_vals[u].end(), greater<int>());

  while (subtree_vals[u].size() > 20) subtree_vals[u].pop_back();

  // cout << "subtree_vals[" << u << "]=" << subtree_vals[u] << endl;

  for (auto d : queries_at_node[u]) {
    int k = d.first;
    int ans = subtree_vals[u][k];
    // cout << "k=" << k << "ans=" << ans << endl;
    queries_at_node[u][d.first] = ans;
  }

}

i32 main() {

  cin >> N >> Q;

  for (int i=1; i<= N; i++) {
    cin >> X[i];
  }

  for (int i=0; i<N-1; i++) {
    int a, b;
    cin >> a >> b;
    neighbours[a].push_back(b);
    neighbours[b].push_back(a);
  }

  for (int q=0; q<Q; q++) {
    int v, k;
    cin >> v >> k;
    queries.push_back({v, k-1});
    queries_at_node[v][k-1] = -1;
  }


  dfs0(1, 1);

  dfs1(1, 1);


  for (auto q : queries) {
    cout << queries_at_node[q.first][q.second] << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS