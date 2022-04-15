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

constexpr int MODULUS = 1000000007;

class DivisorSieve {
public:
  vector<vector<int>> divisors;
  DivisorSieve(size_t N=1e6+10) {
    divisors = vector<vector<int>>(N, vector<int>());
    for (int i=1; i<N; i++) {
      for (int j=i; j<N; j+=i) {
        if (i == j) continue;
        divisors[j].push_back(i);
      }
    }

    for (int i=1; i<N; i++) {
      divisors[i].push_back(i);
      reverse(divisors[i].begin(), divisors[i].end());
    }
  }
};

int N;
vector<int> A;

i32 main() {

  auto s = DivisorSieve();

  cin >> N;
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A.push_back(a);
  }

  auto dp = vector<int>(1e6+10, 0);
  dp[0] = 1;

  // cout << A << endl;

  int ret = 0;

  for (auto a : A) {
    for (auto d : s.divisors[a]) {
      ret += dp[d-1];
      ret %= MODULUS;
      dp[d] += dp[d-1];
      dp[d] %= MODULUS;
    }
  }

  cout << ret << endl;

  return 0;
}
