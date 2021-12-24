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

int N, M, K;

const int INF = 1000000009;
vector<pair<int, int>> adj[200009];
bool relaxed[200009];
int rail_to[200009];
set<int> rail_dests;

void dijkstra(int s, vector<int>& d) {
  d.assign(N, INF);

  using pii = pair<int, int>;
  priority_queue<pii, vector<pii>, greater<pii>> q;

  d[s] = 0;
  q.push({0, s});

  for (auto t : rail_dests) {
    int y = rail_to[t];
    d[t] = y;
    q.push({d[t], t});
  }

  while (!q.empty()) {
    int v = q.top().second;
    int d_v = q.top().first;
    q.pop();
    if (d_v != d[v])
        continue;

    for (auto edge : adj[v]) {
        int to = edge.first;
        int len = edge.second;

        if (d[v] + len <= d[to]) relaxed[to] = true;
        if (d[v] + len < d[to]) {
            d[to] = d[v] + len;
            q.push({d[to], to});
        }
    }
  }
}


i32 main() {

  memset(relaxed, 0, sizeof(relaxed));

  cin >> N >> M >> K;
  for (int i=0; i<N; i++) {
    rail_to[i] = INF;
  }

  for (int i=0; i<M; i++) {
    int u, v, x;
    cin >> u >> v >> x;
    u--; v--;
    adj[u].push_back({v, x});
    adj[v].push_back({u, x});
  }

  for (int i=0; i<K; i++) {
    int s, y;
    cin >> s >> y;
    s--;
    rail_to[s] = min(rail_to[s], y);
    rail_dests.insert(s);
  }

  vector<int> d, p;
  dijkstra(0, d);

  int ret = K - rail_dests.size();

  // cout << "closing" << ret << "redundant" << endl;
  for (auto t : rail_dests) {
    if (relaxed[t]) ret++;
  }
  cout << ret << endl;

  return 0;
}
