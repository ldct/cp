#include <bits/stdc++.h>
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

int N, M;
vector<int> neighbours[5009];

bool visited[5009];

void dfs0(int u, vector<int>& ret, pair<int, int> exclude) {
  if (visited[u]) return;
  visited[u] = true;
  ret.push_back(u);
  for (auto v : neighbours[u]) {
    if (min(u, v) == exclude.first && max(u, v) == exclude.second) continue;
    dfs0(v, ret, exclude);
  }
}

vector<pair<int, int>> edges;

int main() {

  cin >> N >> M;
  for (int i=0; i<M; i++) {
    int u, v;
    cin >> u >> v;
    edges.push_back({min(u, v), max(u, v)});
    neighbours[u].push_back(v);
    neighbours[v].push_back(u);
  }

  for (int i=1; i<=N; i++) sort(neighbours[i].begin(), neighbours[i].end());

  if (N-1 == M) {
    memset(visited, 0, sizeof(visited));
    vector<int> ret;
    dfs0(1, ret, {-1, -1});
    for (auto r : ret) {
      cout << r << " ";
    }
    cout << endl;
  } else {
    vector<vector<int>> candidates;
    for (auto e : edges) {
      memset(visited, 0, sizeof(visited));
      vector<int> r;
      dfs0(1, r, e);
      if (r.size() != N) continue;
      candidates.push_back(r);
    }
    int i = 0;
    for (int j = 1; j<candidates.size(); j++) {
      if (!lexicographical_compare(
        candidates[i].begin(), candidates[i].end(),
        candidates[j].begin(), candidates[j].end()
      )) { i = j; }
    }
    for (auto c : candidates[i]) {
      cout << c << " ";
    }
    cout << endl;
  }

  return 0;
}
