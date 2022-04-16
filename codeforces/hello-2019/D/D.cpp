#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

unordered_map<int, vector<int>> memo1;
map<pair<int, int>, double> memo2;

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

vector<int> get_divisors(int n) {
  if (memo1.count(n)) return memo1[n];
  // cout << n << endl;
  vector<int> ret;
  for (int i=1; i*i <= n; i++) {
    if ((n % i) == 0) {
      ret.push_back(i);
      if (i * i != n) ret.push_back(n / i);
    }
  }
  // return ret;
  return memo1[n] = ret;
}

double ans(int x, int k) {
  if (x == 1) return 1;
  if (k == 0) return double(x);

  pair<int, int> key = {x, k};

  if (memo2.count(key)) return memo2[key];

  auto divisors = get_divisors(x);
  double a = 0;
  int b = 0;
  for (auto d : divisors) {
    auto r = ans(d, k-1);;
    a += r;
    b += 1;
  }
  return memo2[key] = a / double(b);
}


i32 main() {

  int N = 866421317361600;

  auto divisors = get_divisors(N);

  int r = 0;

  // for (auto a : divisors) {
  //   for (int i=1; i*a <= N; i++) {
  //     r++;
  //   }
  // }

  cout << r << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS