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

int N, M, s, t;

vector<int> neighbours[200009];
int level[200009];
vector<pair<pair<int, int>, pair<int, int>>> edges;

int num_shortest[200009];
int num_second[200009];

constexpr int MODULUS = 1000000007;

void prop(int u, int v) {
  if (level[v] < level[u]) return;
  // cout << u << "->" << v << endl;
  if (level[u] != level[v]) {
    num_shortest[v] += num_shortest[u];
    num_shortest[v] %= MODULUS;

    num_second[v] += num_second[u];
    num_second[v] %= MODULUS;
  } else {
    // same level
    num_second[v] += num_shortest[u];
    num_second[v] %= MODULUS;
  }
}

void bfs(int s) {
  set<int> worklist, next_worklist;
  worklist.insert(s);

  int l = 0;
  while (1) {

    assert(next_worklist.size() == 0);

    for (auto u : worklist) {
      if (level[u] != -1) continue;
      level[u] = l;
      for (auto v : neighbours[u]) {
        if (level[v] == -1) {
          next_worklist.insert(v);
        }
      }
    }

    if (next_worklist.size() == 0) break;
    worklist = move(next_worklist);
    l++;
  }
}

i32 main() {

  int T;
  cin >> T;
  while (T --> 0) {
    edges.clear();
    memset(num_shortest, 0, sizeof(num_shortest));
    memset(num_second, 0, sizeof(num_second));

    cin >> N >> M >> s >> t;

    for (int i=1; i<=N; i++) {
      neighbours[i].clear();
      level[i] = -1;
    }

    for (int i=0; i<M; i++) {
      int u, v;
      cin >> u >> v;
      neighbours[u].push_back(v);
      neighbours[v].push_back(u);
      edges.push_back({{-1, -1}, {u, v}});
    }

    bfs(s);

    for (int i=0; i<M; i++) {
      const auto [u, v] = edges[i].second;
      edges[i].first.first = min(level[u], level[v]);
      edges[i].first.second = level[u] + level[v] - min(level[u], level[v]);
    }

    sort(edges.begin(), edges.end());

    num_shortest[s] = 1;

    for (int i=0; i<M; i++) {
      const auto [u, v] = edges[i].second;
      prop(u, v);
      prop(v, u);
    }

    cout << ((num_shortest[t] + num_second[t]) % MODULUS) << endl;
  }


  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS