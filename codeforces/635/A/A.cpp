#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

int N, K;

vector<int> neighbours[200009];
int chosen[200009];
int sz[200009];

vector<pair<pair<int, int>, int>> depths;

int dfs(int u, int parent, int depth) {
  int ret = 1;
  for (auto v : neighbours[u]) {
    if (v == parent) continue;
    ret += dfs(v, u, depth+1);
  }
  sz[u] = ret;
  depths.push_back({{depth -ret, 0}, u});
  return ret;
}

int ret = 0;
void dfs2(int u, int parent, int depth) {
  if (chosen[u]) {
    // cout << "chose " << u << " " << depth << endl;
    ret += depth;
    for (auto v : neighbours[u]) {
      if (v == parent) continue;
      dfs2(v, u, depth);
    }
  } else {
    for (auto v : neighbours[u]) {
      if (v == parent) continue;
      dfs2(v, u, depth+1);
    }
  }
}

i32 main() {

  memset(chosen, 0, sizeof(chosen));

  cin >> N >> K;
  for (int i=0;i<N-1;i++) {
    int u, v;
    cin >> u >> v;
    neighbours[u].push_back(v);
    neighbours[v].push_back(u);
  }

  dfs(1, 1, 0);

  sort(depths.begin(), depths.end());
  reverse(depths.begin(), depths.end());

  // cout << depths << endl;

  for (int i=0; i<K; i++) {
    chosen[depths[i].second] = 1;
  }

  dfs2(1, 1, 0);

  cout << ret << endl;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS