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
  vector<vector<int32_t>> divisors;
  DivisorSieve(size_t N=2e5+10) {
    divisors = vector<vector<int32_t>>(N, vector<int32_t>());
    for (int32_t i=1; i<N; i++) {
      for (int32_t j=i; j<N; j+=i) {
        divisors[j].push_back(i);
      }
    }
  }
};

int N;
vector<int> A;
int freq[200009];

i32 main() {

  memset(freq, 0, sizeof(freq));

  cin >> N;
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A.push_back(a);
    freq[a]++;
  }

  auto sieve = DivisorSieve();

  int ret = 0;
  for (auto a : A) {
    for (auto d : sieve.divisors[a]) {
      ret += freq[d]*freq[a/d];
    }
  }

  cout << ret << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS