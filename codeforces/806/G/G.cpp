#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int N, K;
vector<int> A;

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

int memo[40][100009];

int best(int d, int i) {
  if (i == N) return 0;
  if (d >= 32) return 0;
  if (memo[d][i] != -1) return memo[d][i];

  return memo[d][i] = max(
    -K + (A[i] >> d) + best(d, i+1),
    (A[i] >> (d+1)) + best(d+1, i+1)
  );
}

int solve() {
  for (int d=0; d<35; d++) for (int i=0; i<=N; i++) {
    memo[d][i] = -1;
  }
  return best(0, 0);
}

i32 main() {

  int T;
  cin >> T;
  while (T --> 0) {
    cin >> N >> K;
    A.clear();
    for (int i=0; i<N; i++) {
      int a;
      cin >> a;
      A.push_back(a);
    }
    cout << solve() << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS