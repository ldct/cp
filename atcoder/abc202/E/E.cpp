#include <bits/stdc++.h>
using namespace std;

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class K, class V> ostream& operator << (ostream& os, const map<K, V>& myMap) {
    os << "{";
    for(auto it = myMap.cbegin(); it != myMap.cend(); ++it) {
      os << it->first << ":" << it->second << " ";
    }
    os << "}";
    return os;
  }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

int N, Q;
vector<int> children[200009];
map<int, int> queries_at_node[200009];
vector<pair<int, int>> queries;
int depth[200009];
map<int, int>* descendents[200009];

void dfs0(int u, int d) {
  depth[u] = d;
  for (auto v : children[u]) {
    dfs0(v, d+1);
  }
}
void dfs(int u) {
  for (auto v : children[u]) {
    dfs(v);
  }

  map<int, int>* largest = descendents[u];

  for (auto v : children[u]) {
    if (!largest) {
      largest = descendents[v];
    } else {
      if (descendents[v]->size() > largest->size()) {
        largest = descendents[v];
      }
    }
  }

  for (auto v : children[u]) {
    if (descendents[v] == largest) continue;
    // merge descendents[v] into largest
    for(auto it = (*descendents[v]).cbegin(); it != (*descendents[v]).cend(); ++it) {
      // cout << it->first << endl;
      (*largest)[it->first] += it->second;
    }
  }

  if (descendents[u] != largest) {
    // merge descendents[u] into largest
    for(auto it = (*descendents[u]).cbegin(); it != (*descendents[u]).cend(); ++it) {
      (*largest)[it->first] += it->second;
    }
  }

  descendents[u] = largest;

  // cout << "answering query " << u << " " << (*descendents[u]) << endl;

  for (auto d : queries_at_node[u]) {
    int ans = (*descendents[u])[d.first];
    queries_at_node[u][d.first] = ans;
  }
}

int main() {

  cin >> N;

  for (int i=0; i<N; i++) descendents[i] = new map<int, int>();

  for (int i=1; i<N; i++) {
    int p;
    cin >> p;
    p--;
    children[p].push_back(i);
  }

  dfs0(0, 0);

  for (int i=0; i<N; i++) {
    (*(descendents[i]))[depth[i]] = 1;
  }

  cin >> Q;

  for (int q=0; q<Q; q++) {
    int u, d;
    cin >> u >> d;
    u--;
    queries.push_back({u, d});
    queries_at_node[u][d] = -1;
  }

  dfs(0);

  for (auto q : queries) {
    cout << queries_at_node[q.first][q.second] << endl;
  }

  return 0;
}
