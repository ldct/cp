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

int N;
vector<int> children[5000];
string colour;
int black[5000];
int white[5000];

pair<int, int> dfs(int u) {
  auto ret = pair<int, int>();

  if (colour[u-1] == 'B') {
    ret.first++;
  } else {
    ret.second++;
  }

  // cout << u << endl;
  for (auto v : children[u]) {
    auto r = dfs(v);
    ret.first += r.first;
    ret.second += r.second;
  }

  black[u] = ret.first;
  white[u] = ret.second;

  return ret;
}

i32 main() {

  int T;
  cin >> T;
  while (T --> 0) {
    cin >> N;
    for (int i=0; i<=N; i++) {
      children[i].clear();
    }
    for (int i=1; i<=N-1; i++) {
      int a; cin >> a;
      children[a].push_back(i+1);
    }
    cin >> colour;
    dfs(1);

    int ret = 0;
    for (int i=1; i<=N; i++) {
      if (black[i] == white[i]) ret++;
    }
    cout << ret << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS