#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>
#include <queue>

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

int N, C;

vector<pair<long long, long long>> adj[400009];

void dijkstra(long long N, long long s, vector<long long>& d, bool reverse) {
  d.assign(N, LLONG_MAX);

  using pii = pair<long long, long long>;
  priority_queue<pii, vector<pii>, greater<pii>> q;

  d[s] = 0;
  q.push({0, s});

  while (!q.empty()) {
    long long v = q.top().second;
    long long d_v = q.top().first;
    q.pop();
    if (d_v != d[v])
        continue;

    for (auto edge : adj[v]) {
        long long to = edge.first;
        long long len = edge.second;

        if (d[v] + len < d[to]) {
            d[to] = d[v] + len;
            q.push({d[to], to});
        }
    }
}
}

int shadow(int x) {
  return N+x;
}

i32 main() {

  cin >> N >> C;
  for (int i=0; i<N-1; i++) {
    int a;
    cin >> a;
    int j = i+1;
    adj[i].push_back({j, a});
    adj[j].push_back({i, a});
  }
  for (int i=0; i<N; i++) {
    int j = shadow(i);
    adj[i].push_back({j, C});
    adj[j].push_back({i, 0});
  }
  for (int i=0; i<N-1; i++) {
    int b;
    cin >> b;
    int j = i+1;
    adj[shadow(i)].push_back({shadow(j), b});
    adj[shadow(j)].push_back({shadow(i), b});
  }

  auto d = vector<int>(2*N, 0);
  dijkstra(2*N, 0, d, false);

  // cout << d << endl;

  for (int i=0; i<N; i++) {
    cout << d[i] << " ";
  }
  cout << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS