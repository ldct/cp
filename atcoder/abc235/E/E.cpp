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

struct UF {
  vector<int> e;
  UF(int n) : e(n, -1) {}
  bool sameSet(int a, int b) { return find(a) == find(b); }
  int size(int x) { return -e[find(x)]; }
  int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
  bool join(int a, int b) {
    a = find(a), b = find(b);
    if (a == b) return false;
    if (e[a] > e[b]) swap(a, b);
    e[a] += e[b]; e[b] = a;
    return true;
  }
};

int N, M, Q;
vector<pair<pair<int, int>, pair<int, int>>> edges;
bool ans[200009];

i32 main() {

  cin >> N >> M >> Q;

  auto uf = UF(N+1);

  while (M --> 0) {
    int a, b, c;
    cin >> a >> b >> c;
    edges.push_back({{c, -1}, {a, b}});
  }

  for (int q=0; q<Q; q++) {
    int a, b, c;
    cin >> a >> b >> c;
    edges.push_back({{c, q}, {a, b}});
  }

  sort(edges.begin(), edges.end());

  for (auto edge : edges) {
    auto a = edge.second.first;
    auto b = edge.second.second;

    if (edge.first.second == -1) {
      uf.join(a, b);
    } else {
      ans[edge.first.second] = uf.find(a) == uf.find(b);
    }
  }

  for (int i=0; i<Q; i++) {
    cout << (ans[i] ? "No" : "Yes") << endl;
  }

  return 0;
}
