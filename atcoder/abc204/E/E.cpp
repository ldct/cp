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

#define int long long

const int INF = 1000000000;
vector<tuple<int, int, int>> adj[100009];
int N, M;

void dijkstra(int s, vector<int> & d, int wf) {
  int n = N;
  d.assign(n, INF);
  d[s] = wf;
  using pii = pair<int, int>;
  priority_queue<pii, vector<pii>, greater<pii>> q;
  q.push({wf, s});
  while (!q.empty()) {
      int v = q.top().second;
      int d_v = q.top().first;
      q.pop();
      if (d_v != d[v])
          continue;

      for (auto edge : adj[v]) {
          int to = get<0>(edge);
          int C = get<1>(edge);
          int D = get<2>(edge);

          int len = C + (D / (d_v + 1));
          if (d[v] + len < d[to]) {
              d[to] = d[v] + len;
              q.push({d[to], to});
          }
      }
  }
}

int ans(int wf) {
  vector<int> ret;
  dijkstra(0, ret, wf);
  return ret[N-1];
}

int32_t main() {

  cin >> N >> M;
  for (int i=0; i<M; i++) {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    a--; b--;
    adj[a].push_back({b, c, d});
  }

  if (ans(1000000) == INF) {
    cout << -1 << endl;
    return 0;
  }

  for (int i=0;; i++) {
    int a = ans(i), b = ans(i+1);
    if (b > a) {
      cout << a << endl;
      return 0;
    }
  }

}
