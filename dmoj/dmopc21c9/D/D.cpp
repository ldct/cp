#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int N, M;
string _S;
vector<int> S;
vector<int> dir;
vector<int> indegree;

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

i32 main() {

  cin >> N >> M;
  assert(N == 1);

  cin >> _S;
  M = _S.size();

  indegree = vector<int>(M, 0);

  S.clear(); for (int i=0; i<_S.size(); i++) S.push_back(_S[i] == 'H' ? 0 : 1);

  for (int i=0; i<S.size()-1; i++) {
    if (S[i] == 0) {
      dir.push_back(0);
      indegree[i+1]++;
      S[i+1] = 1-S[i+1];
    } else {
      dir.push_back(1);
      indegree[i]++;
    }
  }

  S.clear(); for (int i=0; i<_S.size(); i++) S.push_back(_S[i] == 'H' ? 0 : 1);
  auto ret = vector<int>();

  vector<int> worklist;
  auto present = vector<int>(M, 1);
  bool works = true;

  for (int i=0; i<M; i++) {
    if (indegree[i] == 0) worklist.push_back(i);
  }

  while (worklist.size()) {
    auto u = worklist[worklist.size()-1];
    worklist.pop_back();

    // flip u

    if (S[u] != 0) {
      works = false;
      break;
    }

    ret.push_back(u);
    present[u] = 0;

    for (auto v : {u-1, u+1}) {
      if (!(0 <= v && v < M)) continue;
      if (!present[v]) continue;
      S[v] = 1-S[v];
      indegree[v]--;
      if (indegree[v] == 0) worklist.push_back(v);
    }
  }

  if (!(works && ret.size() == M)) {
    cout << (-1) << endl; return 0;
  }

  for (auto i : ret) {
    cout << 1 << " " << (i+1) << endl;
  }
  return 0;
}
