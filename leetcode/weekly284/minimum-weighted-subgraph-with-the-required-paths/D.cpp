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

vector<pair<long long, long long>> adj[100009];
vector<pair<long long, long long>> opp_adj[100009];

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

    if (!reverse) {
      for (auto edge : adj[v]) {
          long long to = edge.first;
          long long len = edge.second;

          if (d[v] + len < d[to]) {
              d[to] = d[v] + len;
              q.push({d[to], to});
          }
      }
    } else {
      for (auto edge : opp_adj[v]) {
          long long to = edge.first;
          long long len = edge.second;

          if (d[v] + len < d[to]) {
              d[to] = d[v] + len;
              q.push({d[to], to});
          }
      }
    }

  }
}

class Solution {
public:
    long long minimumWeight(int n, vector<vector<int>>& edges, int src1, int src2, int dest) {

      for (int i=0; i<n; i++) {
        adj[i].clear();
        opp_adj[i].clear();
      }


      for (auto& e : edges) {
        int u = e[0];
        int v = e[1];
        int w = e[2];
        adj[u].push_back({v, w});
        opp_adj[v].push_back({u, w});
      }

      vector<long long> d1, d2, d3;

      dijkstra(n, src1, d1, false);
      dijkstra(n, src2, d2, false);
      dijkstra(n, dest, d3, true);

      long long ret = LLONG_MAX;

      for (int i=0; i<n; i++) {
        if (d1[i] == LLONG_MAX) continue;
        if (d2[i] == LLONG_MAX) continue;
        if (d3[i] == LLONG_MAX) continue;

        long long candidate = d1[i] + d2[i] + d3[i];
        ret = min(ret, candidate);
      }

      if (ret == LLONG_MAX) return -1;


      return ret;
    }
};

int main() {

  vector<vector<int>> edges1;

  edges1.push_back({0,2,2}) ;
  edges1.push_back({0,5,6});
  edges1.push_back({1,0,3});
  edges1.push_back({1,4,5});
  edges1.push_back({2,1,1});
  edges1.push_back({2,3,3});
  edges1.push_back({2,3,4});
  edges1.push_back({3,4,2});
  edges1.push_back({4,5,1});

  vector<vector<int>> edges2;
  edges2.push_back({0,1,1});
  edges2.push_back({2,1,1});

  auto s = Solution();
  cout << s.minimumWeight(
    6,
    edges1,
    0,
    1,
    5
  ) << endl;

  cout << s.minimumWeight(
    3,
    edges2,
    0,
    1,
    2
  );

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS