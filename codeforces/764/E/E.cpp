int N, M;
string target;
set<string> valid;
map<string, pair<int, int>> lookup;
// vector<string> initial_strings;

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

bool truthy(pair<int, pair<int, int>> p) {
  if (p.first == -1) return true;
  if (p.first == -2) return false;
  return true;
}

pair<int, pair<int, int>> memo[1009];

pair<int, pair<int, int>> ok(int i) {
  if (i == target.size()) return {-1, {-1, -1}}; // true
  if (memo[i].first != -3) return memo[i];
  for (int j=2; j<=3; j++) {
    string ss = target.substr(i, j);
    if (valid.count(ss) && truthy(ok(i + ss.size()))) {
      auto p = lookup[ss];
      return memo[i] = {p.first, {p.second, ss.size()}};
    }
  }
  return memo[i] = {-2, {-1, -1}}; // false
}

i32 main() {
  int T;
  cin >> T;

  while (T --> 0) {

    valid.clear(); lookup.clear();

    cin >> N >> M;

    for (int i=0; i<=M+2; i++) {
      memo[i] = {-3, {-1, -1}};
    }

    for (int i=0; i<N; i++) {
      string S;
      cin >> S;

      for (int j=0; j<S.size(); j++) for (int l=2; l<=3; l++) {
        string ss = S.substr(j, l);
        if (ss.size() >= 2) {
          valid.insert(ss);
          lookup[ss] = {i, j};
        }
      }
    }

    cin >> target;
    if (!truthy(ok(0))) {
      cout << -1 << endl;
    } else {
      vector<pair<int, pair<int, int>>> ret;

      int i = 0;
      while (i != M) {
        auto p = ok(i);
        ret.push_back(p);
        i += ok(i).second.second;
      }

      cout << ret.size() << endl;

      for (auto p : ret) {
        cout << (1 + p.second.first) << " " << (p.second.first + p.second.second) << " " << (p.first+1) << endl;
      }

    }
  }

  return 0;
}
