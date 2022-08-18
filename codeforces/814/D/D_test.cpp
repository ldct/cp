#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>

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
vector<int> A;

constexpr int MAX_X = 4096;

short memo[5009][MAX_X];

short ans(short i, short x) {
  if (i == A.size()) return 0;

  if (memo[i][x] != -1) return memo[i][x];

  short a = A[i];
  short b = a^x;

  if (i == A.size()-1) {
    if (b == 0) return 0;
    return 1;
  }
  if (b == 0) return ans(i + 1, 0);

  short ret = min(
    1 + ans(i+1, 0),
    1 + ans(i+1, b)
  );

  return memo[i][x] = ret;
}



i32 main() {

  int T = 500;

  while (T --> 0) {
    A.clear();
    N = 100;

    for (int i=0; i<N; i++) {
      for (int x=0; x<MAX_X; x++) {
        memo[i][x] = -1;
      }
    }

        memset(memo, -1, sizeof(memo));


    for (int i=0; i<N; i++) {
      A.push_back(i);
    }

    // cout << A << endl;
    cout << ans(0, 0) << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS