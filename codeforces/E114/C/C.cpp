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

int N, M;
vector<long long> A;
long long TOTAL;

long long score(int idx, long long x, long long y) {
  if (!(0 <= idx && idx < A.size())) return LLONG_MAX;

  long long ca;
  if (A[idx] >= x) {
    ca = 0;
  } else {
    ca = x - A[idx];
  }

  long long cd;
  long long rest = TOTAL - A[idx];

  if (rest >= y) {
    cd = 0;
  } else {
    cd = y - rest;
  }

  return ca + cd;
}

int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N;
  for (int i=0; i<N; i++) {
    long long a;
    cin >> a;
    A.push_back(a);
  }
  sort(A.begin(), A.end());
  TOTAL = 0;
  for (const auto a : A) TOTAL += a;

  cin >> M;
  for (int m=0; m<M; m++) {
    long long x, y;
    cin >> x >> y;

    int i = (lower_bound(A.begin(), A.end(), x) - A.begin());

    long long ret = LLONG_MAX;
    ret = min(ret, score(i-1, x, y));
    ret = min(ret, score(i, x, y));
    ret = min(ret, score(i-1, x, y));
    ret = min(ret, score(i, x, y));

    cout << ret << endl;
  }

  return 0;
}
