#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

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

int N, K;
vector<pair<int, int>> grass;
vector<int> prefix;

bool ok(int i, int j) {
  int x1 = grass[i].first;
  int x2 = grass[j].first;
  return (x2 - x1 <= 2*K);
}

int score(int i, int j) {
  return prefix[j+1] - prefix[i];
}

i32 main() {
  int g,x,i;

  freopen("lazy.in", "r", stdin);
  freopen("lazy.out", "w", stdout);

  scanf("%lld %lld", &N, &K);

  for (i = 0; i < N; i++) {
    scanf("%lld %lld", &g, &x);
    grass.push_back({x, g});
  }

  sort(grass.begin(), grass.end());
  prefix.push_back(0);
  for (auto p : grass) {
    prefix.push_back(prefix[prefix.size()-1] + p.second);
  }

  int ret = 0;

  int j = 0;
  for (int i=0; i<grass.size(); i++) {
    int x1 = grass[i].first;
    while (j < grass.size()-1 && ok(i, j+1)) j++;
    ret = max(ret, score(i, j)) ;
  }

  cout << ret << endl;

  return 0;
}
