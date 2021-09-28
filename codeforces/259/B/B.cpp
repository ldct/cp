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
vector<int> A;
vector<int> PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61};
vector<int> FACTORS = vector<int>(62, -1);

int memo[109][1 << 18];
int parent[109][1 << 18];

int bits_factorize(int n) {
  int ret = 0;
  for (int i=0; i<PRIMES.size(); i++) {
    if (n % PRIMES[i] == 0) {
      ret |= (1 << i);
    }
  }
  return ret;
}

bool clashes(int avoid, int k) {
  return (avoid & FACTORS[k]) > 0;
}

int min_score(int i, int avoid) {
  if (i == A.size()) return 0;
  if (memo[i][avoid] != -1) return memo[i][avoid];

  int ret_score = INT_MAX;

  for (int k=1; k<=2*A[i]; k++) {
    if (clashes(avoid, k)) continue;
    auto score = min_score(i+1, avoid | FACTORS[k]);
      if (abs(k-A[i]) + score < ret_score) {
          ret_score = abs(k-A[i])+score;
          parent[i][avoid] = k;
      }
  }
  return memo[i][avoid] = ret_score;
}

int main() {

  memset(memo, -1, sizeof(memo));

  for (int i=1; i<62; i++) {
    FACTORS[i] = bits_factorize(i);
  }

  cin >> N;

  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A.push_back(a);
  }

  min_score(0, 0);

  vector<int> ret;

  int k = 0;
  int avoid = 0;
  for (int i=0; i<A.size(); i++) {
    k = parent[i][avoid];
    avoid = avoid | FACTORS[k];
    cout << k;
    if (i != A.size()-1) cout << " ";
  }
  cout << endl;

  return 0;
}
