#include <bits/stdc++.h>
using namespace std;

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

constexpr int MODULUS = 1000000007;
constexpr int MAX_BIT = 32;

long long modexp(long long b, long long e) {
	long long ans = 1;
	for (; e; b = b * b % MODULUS, e /= 2)
		if (e & 1) ans = ans * b % MODULUS;
	return ans;
}

long long coz(vector<long long>& n) {
  for (auto v : n) assert(v >= 0);
  long long ret = 0;
  for (int i=0; i<n.size(); i++) {
    ret |= n[i];
  }
  ret *= modexp(2, n.size()-1);
  ret %= MODULUS;
  return ret;
}

int ans(int N, vector<tuple<long long, long long,long long>>& constraints) {
  auto big_arr = vector<long long>(N, 0);
  for (int b=0; b<MAX_BIT; b++) {
    auto paint = vector<long long>(N+1, 0);
    for (auto [l, r, x] : constraints) {
      if (0 == (x & (1 << b))) {
        paint[l] += 1;
        paint[r+1] -= 1;
      }
    }
    vector<long long> _arr;
    _arr.push_back(0);
    for (auto p : paint) {
      _arr.push_back(_arr[_arr.size()-1] + p);
    }
    vector<long long> arr;
    for (int i=0; i<N; i++) {
      int x = _arr[i+1];
      int y = (x == 0) ? 1 : 0;
      if (y == 1) {
        // cout << "add" << i << b << endl;
        big_arr[i] += (1LL << b);
      }
    }
    // cout << big_arr << endl;
  }
  return coz(big_arr) % MODULUS;
}

int main() {

  int T;
  cin >> T;
  while (T --> 0) {
    int N, M;
    cin >> N >> M;
    vector<tuple<long long,long long,long long>> constraints;
    while (M --> 0) {
      long long l, r, x;
      cin >> l >> r >> x;
      l--; r--;
      constraints.push_back({l, r, x});
    }
    cout << ans(N, constraints) << endl;
  }

  return 0;
}
