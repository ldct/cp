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
vector<int> A;
int memo[11][11][11][11][11][11][11][11][11][11][20];

vector<int> base(int n) {
  auto ret = vector<int>();
  while (n > 0) {
    ret.push_back(n % 10);
    n /= 10;
  }
  reverse(ret.begin(), ret.end());
  return ret;
}

bool all0(vector<int> arr) {
  for (auto d : arr) if (d != 0) return false;
  return true;
}

int count(vector<int> prefix, int rest);
int count0(int rest);

int count_dp(
  int A0, int A1, int A2, int A3, int A4, int A5, int A6, int A7, int A8, int A9,
  int r
) {
  if (r == 0) {
    if (A0*A1*A2*A3*A4*A5*A6*A7*A8*A9 == 0) return 0;
    return 1;
  }

  if (memo[A0+1][A1+1][A2+1][A3+1][A4+1][A5+1][A6+1][A7+1][A8+1][A9+1][r] != -1) return memo[A0+1][A1+1][A2+1][A3+1][A4+1][A5+1][A6+1][A7+1][A8+1][A9+1][r];

  int ret = 0;
  for (int d=0; d<10; d++) {

    ret += count_dp(
      d == 0 && A0 >= 0 ? A0 - 1 : A0,
      d == 1 && A1 >= 0 ? A1 - 1 : A1,
      d == 2 && A2 >= 0 ? A2 - 1 : A2,
      d == 3 && A3 >= 0 ? A3 - 1 : A3,
      d == 4 && A4 >= 0 ? A4 - 1 : A4,
      d == 5 && A5 >= 0 ? A5 - 1 : A5,
      d == 6 && A6 >= 0 ? A6 - 1 : A6,
      d == 7 && A7 >= 0 ? A7 - 1 : A7,
      d == 8 && A8 >= 0 ? A8 - 1 : A8,
      d == 9 && A9 >= 0 ? A9 - 1 : A9,
      r-1
    );
  }
  return memo[A0+1][A1+1][A2+1][A3+1][A4+1][A5+1][A6+1][A7+1][A8+1][A9+1][r] = ret;
}

int count0(int rest) {
  if (rest == 0) return 0;
  int ret = count0(rest-1);
  for (int d=1; d<10; d++) {
    vector<int> p = {d};
    ret += count(p, rest-1);
  }
  return ret;
}

int count(vector<int> prefix, int rest) {
  if (all0(prefix)) return count0(rest);

  vector<int> _A = vector<int>(A);
  for (auto d : prefix) {
    if (_A[d] >= 0) _A[d] -= 1;
  }
  return count_dp(
    _A[0], _A[1], _A[2], _A[3], _A[4], _A[5], _A[6], _A[7], _A[8], _A[9],
    rest
  );
}

int num_loves(int _N) {
  auto N = base(_N);

  int ret = 0;

  for (int i=0; i<N.size(); i++) {
    vector<int> prefix;
    for (int j=0; j<i; j++) { prefix.push_back(N[j]); }
    int x = N[i];
    int rest = N.size() - prefix.size() - 1;

    for (int j=0; j<x; j++) {
      prefix.push_back(j);
      ret += count(prefix, rest);
      prefix.pop_back();
    }
  }

  return ret;
}

i32 main() {

  int T;
  cin >> T;

  while (T --> 0) {
    memset(memo, -1, sizeof(memo));
    cout << "memset done" << endl;

    int L, R;
    cin >> L >> R;
    A.clear();
    for (int i=0; i<10; i++) {
      int a; cin >> a; A.push_back(a);
    }
    cout << (num_loves(R+1) - num_loves(L)) << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS