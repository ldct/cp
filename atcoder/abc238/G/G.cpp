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


class Sieve {
public:
  vector<int> s;
  Sieve(size_t N=1000009) {
    s = vector<int>(N, -1);
    s[0] = 0;
    s[1] = 0;
    for (int i=2; i*i < N; i++) {
      if (s[i] != -1) continue;
      for (int j = i; j < N; j += i) {
        if (j > i) s[j] = i;
      }
    }
  }
  int count_primes() {
    int ret=0;
    for (auto f : s) if (f == -1) ret += 1;
    return ret;
  }

  vector<int> prime_factors(int x) {
    vector<int> ret;
    if (s[x] == -1) {
      ret.push_back(x);
      return ret;
    }
    auto p = s[x];
    while (x % p == 0) {
      ret.push_back(p);
      x /= p;
    }
    if (x == 1) return ret;
    for (auto q : prime_factors(x)) {
      ret.push_back(q);
    }
    return ret;
  }
};

constexpr int MAX_A = 1000000;

// only index into prime entries
int X[3][1000009];
int prime_idx[1000009];

int A[200009];
int key[200009];
int key_prefix[200009];

int N, Q;

i32 main() {

  memset(prime_idx, 0, sizeof(prime_idx));
  memset(key, 0, sizeof(key));

  auto sieve = Sieve();

  for (int i=0; i<=MAX_A; i++) {
    X[0][i] = rand();
    X[1][i] = rand();
    X[2][i] = X[0][i]^X[1][i];
  }

  cin >> N >> Q;
  for (int i=0; i<N; i++) cin >> A[i];

  for (int i=0; i<N; i++) {
    if (A[i] == 1) continue;

    for (auto p : sieve.prime_factors(A[i])) {
      key[i] ^= X[prime_idx[p] % 3][p];
      prime_idx[p]++;
    }
  }

  key_prefix[0] = 0;
  for (int i=0; i<N; i++) {
    key_prefix[i+1] = key_prefix[i] ^ key[i];
  }

  while (Q --> 0) {
    int l, r;
    cin >> l >> r;
    l--;

    if (key_prefix[l] == key_prefix[r]) {
      cout << "Yes" << endl;
    } else {
      cout << "No" << endl;
    }
    // cout << l << " " << r << "; ";
    // int range_total = 0;
    // for (int x=l; x<r; x++) {
    //   if (A[x] != 1) range_total ^= key[x];
    //   cout << A[x] << " ";
    // }
    // cout << " ;" << range_total << " " << (key_prefix[l] ^ key_prefix[r]) << endl;
  }



  return 0;
}
