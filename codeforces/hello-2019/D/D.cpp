#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

// todo: try hashmap memoization

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

vector<int> PRIMES;

long long modexp(long long b, long long e) {
	long long ans = 1;
	for (; e; b = b * b % MODULUS, e /= 2)
		if (e & 1) ans = ans * b % MODULUS;
	return ans;
}

long long modinv(int a, int b) {
	int b0 = b, t, q;
	int x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}

int N, K;

int memo[50][50][10009];

int ans_pe(int p, int e, int k) {
  if (memo[p][e][k] != -1) return memo[p][e][k];

  if (k == 0) return modexp(PRIMES[p], e);
  vector<int> ep;
  for (int f=0; f<=e; f++) {
    ep.push_back(ans_pe(p, f, k-1));
  }
  int ret = 0;
  for (auto r : ep) {
    ret += r;
    ret %= MODULUS;
  }
  ret *= modinv(ep.size(), MODULUS);
  ret %= MODULUS;
  return memo[p][e][k] = ret;
}

pair<vector<int>, vector<int>> factorize(int n) {
  vector<int> primes;
  vector<int> exponents;
  int p = 2;
  while (n > 1) {
    if (p * p > n) {
      primes.push_back(n);
      exponents.push_back(1);
      return {primes, exponents};
    }
    int e = 0;
    while (n % p == 0) {
      n /= p;
      e++;
    }
    if (e > 0) {
      primes.push_back(p);
      exponents.push_back(e);
    }
    p++;
  }
  return {primes, exponents};
}

int ans(int n, int k) {
  auto f = factorize(n);
  // cout << f.first << endl;
  // cout << f.second << endl;
  PRIMES = f.first;

  // cout << PRIMES << endl;

  int ret = 1;
  for (int i=0; i<f.first.size(); i++) {
    auto p = f.first[i];
    auto e = f.second[i];
    ret *= ans_pe(i, e, k);
    ret %= MODULUS;
  }
  return ret;
}

i32 main() {

  memset(memo, -1, sizeof(memo));

  int N, K;
  cin >> N >> K;
  cout << ans(N, K) << endl;

  return 0;
}
