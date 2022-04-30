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

i32 N, _N, M;

i32 _m[10009];
i32 _a[10009];
i32 m[10000009];

constexpr int MAX_DEPTH = 25;

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

vector<int> decompose(int N) {
  vector<int> ret;

  for (int i=1; N > i; i*=2) {
    ret.push_back(i);
    N -= i;
  }

  if (N > 0) ret.push_back(N);

  return ret;
}
i32 main() {

  ios_base::sync_with_stdio(false); cin.tie(NULL);

  cin >> _N >> M;
  N = MAX_DEPTH*_N;
  for (int i=0; i<_N; i++) {
    cin >> _m[i];
  }

  for (int i=0; i<_N; i++) {
    cin >> _a[i];
    _a[i] = min(_a[i], M);
  }

  for (int i=0; i<_N; i++) {
    auto r = decompose(_a[i]);
    while (r.size() != MAX_DEPTH) r.push_back(0);
    for (int j=0; j<r.size(); j++) {
      m[MAX_DEPTH*i+j] = _m[i]*r[j];
    }
  }

  // for (int i=0; i<N; i++) {
  //   cout << m[i] << " ";
  // }

  auto indexes = ss_ncp();

  auto ret = vector<int>(_N, 0);

  for (auto i : indexes) {
    auto base_index = i / MAX_DEPTH;
    auto base_mass = _m[base_index];
    auto copies = m[i] / base_mass;
    ret[base_index] += copies;
  }

  for (auto r : ret) {
    cout << r << " ";
  }
  cout << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS