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

int N, M;
i32 m[100009];

vector<int> ss_ncp() {
  int target = M;
  auto possible = vector<i64>(target+1, 0);
  possible[0] = 1;
  auto component = vector<i64>(target+1, 0);

  for (int i=0; i<N; i++) {
    auto b = m[i];
    for (int mass=M; mass != -1; mass--) {
      if (
        (possible[mass] == 1) &&
        (mass + b <= target) &&
        (possible[mass+b] == 0)
      ) {
        possible[mass+b] = 1;
        component[mass+b] = b;
      }
    }
  }

  int i;
  for (i=target; i != -1; i--) {
    if (possible[i]) break;
  }

  vector<int> _masses;
  while (i != 0) {
    _masses.push_back(component[i]);
    i -= component[i];
  }

  auto indexes = unordered_map<int, vector<int>>();
  for (int i=0; i<N; i++) {
    auto b = m[i];
    indexes[b].push_back(i);
  }

  auto masses = unordered_map<int, int>();

  for (auto m : _masses) {
    masses[m]++;
  }

  auto ret = vector<int>();

  for (auto m : masses) {
    auto f = m.second;
    for (int i=0; i<f; i++) {
      ret.push_back(indexes[m.first][i]);
    }
  }

  sort(ret.begin(), ret.end());

  return ret;
}

i32 main() {

  ios_base::sync_with_stdio(false); cin.tie(NULL);


  cin >> N >> M;
  for (int i=0; i<N; i++) {
    cin >> m[i];
  }

  auto ret = ss_ncp();
  cout << ret.size() << endl;
  for (auto r : ret) {
    cout << (r+1) << " ";
  }
  cout << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS