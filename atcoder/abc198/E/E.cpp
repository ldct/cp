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

int N;
int colour[100009];
vector<int> neighbours[100009];
int is_good[100009];

unordered_map<int, int> ancestors;

void dfs0(int u, int parent) {

  if (ancestors[colour[u]]) is_good[u] = false;
  ancestors[colour[u]]++;

  for (const auto v : neighbours[u]) {
    if (v == parent) continue;
    dfs0(v, u);
  }

  ancestors[colour[u]]--;
}

int main() {

  cin >> N;
  for (int i=0; i<N; i++) cin >> colour[i];

  for (int i=0; i<N-1; i++) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    neighbours[u].push_back(v);
    neighbours[v].push_back(u);
  }

  for (int i=0; i<N; i++) is_good[i] = true;

  dfs0(0, -1);

  for (int i=0; i<N; i++) {
    if (is_good[i]) cout << (i+1) << endl;
  }



  return 0;
}
