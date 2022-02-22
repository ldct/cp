#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

constexpr int MAX_X = 1000009;

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

bool visited[1009][1009];

vector<pair<int, int>> cells_with[1000009];

int M, N;

void dfs(int x, int y) {
  if (visited[x][y]) return;
  visited[x][y] = true;
  for (auto p : cells_with[x*y]) {
    dfs(p.first, p.second);
  }
}

i32 main() {
  memset(visited, 0, sizeof(visited));

  cin >> M >> N;

  for (int i=1; i<=M; i++) for (int j=1; j<=N; j++) {
    int x;
    cin >> x;
    cells_with[x].push_back({i, j});
  }

  dfs(M, N);

  if (visited[1][1]) {
    cout << "yes" << endl;
  } else {
    cout << "no" << endl;
  }

  return 0;
}
