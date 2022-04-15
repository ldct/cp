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

class DivisorSieve {
public:
  vector<vector<i32>> divisors;
  DivisorSieve(size_t N=1e6+10) {
    divisors = vector<vector<i32>>(N, vector<i32>());
    for (i32 i=1; i<N; i++) {
      for (i32 j=i; j<N; j+=i) {
        divisors[j].push_back(i);
      }
    }
  }
};

int N;
vector<int> A;

i32 main() {

  ios_base::sync_with_stdio(false); cin.tie(NULL);

  int max_A = 1;
  cin >> N;
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A.push_back(a);
    max_A = max(max_A, a);
  }

  reverse(A.begin(), A.end());

  auto dp = vector<i32>(max_A+10, 0);

  for (auto a : A) {
    for (i32 i=1; i*a <= max_A; i++) {
      dp[a] = max(dp[a], 1 + dp[i*a]);
    }
  }

  i32 ret = 0;
  for (auto r : dp) ret = max(ret, r);

  cout << ret << endl;

  return 0;
}
