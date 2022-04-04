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

constexpr int MAX_N = 1009;

int N;
int F[1009];
vector<int> children[MAX_N];

int dfs(int u) {
  if (children[u].size() == 0) return F[u];

  vector<int> cv;

  for (auto v : children[u]) {
    cv.push_back(dfs(v));
  }

  sort(cv.begin(), cv.end());
  cv[0] = max(cv[0], F[u]);

  int ret = 0;
  for (auto c : cv) ret += c;

  return ret;
}

i32 main() {

  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
    cin >> N;
    for (int i=0; i<=N; i++) children[i].clear();
    F[0] = 0;
    for (int i=1; i<=N; i++) cin >> F[i];
    for (int i=1; i<=N; i++) {
      int p;
      cin >> p;
      children[p].push_back(i);
    }
    cout << "Case #" << t << ": " << dfs(0) << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS