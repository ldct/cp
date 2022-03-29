#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

int T, N, K;
vector<int> Xs;
vector<int> Ys;

int memo0[100009];
int memo[5009][5009];

int ans_t1(int i) {
  if (i >= N) return 0;
  if (i == N-1) return Ys[i];

  if (memo0[i] != -1) return memo0[i];

  int ret = Ys[i] + ans_t1(i+1);

  if (Xs[i+1] - Xs[i] <= K) ret = min(ret, ans_t1(i+2));

  if (i+2 < N && (Xs[i+2] - Xs[i] <= K)) ret = min(ret, Ys[i+1] + ans_t1(i+3));

  return memo0[i] = ret;
}

bool far(int i, int j) {
  if (j == -1) return true;
  return Xs[i] - Xs[j] > K;
}

int ans(int i, int j) {
  if (i == N) return 0;
  if (i == N-1) {
    if (!far(i, j)) return LLONG_MIN;
    return Ys[i];
  }

  if (j != -1 && memo[i][j] != -1) return memo[i][j];


  int ret = LLONG_MIN;

  if (i + 2 <= N && (Xs[i+1] - Xs[i] <= K)) ret = max(ret, ans(i+2, j)); // match i, i+1
  if (far(i, j)) ret = max(ret, Ys[i] + ans(i+1, i)); // leave i unmatched
  if (
    i+2 < N
    && (Xs[i+2] - Xs[i] <= K)
    && far(i+1, j)
  ) ret = max(ret, Ys[i+1] + ans(i+3, i+1)); // match i, i+2

  if (j != -1) memo[i][j] = ret;
  return ret;
}

i32 main() {

  cin >> T >> N >> K;

  for (int i=0; i<N; i++) {
    int x, y;
    cin >> x >> y;
    Xs.push_back(x);
    Ys.push_back(y);
  }

  if (T == 1) {
    memset(memo0, -1, sizeof(memo0));
    cout << ans_t1(0) << endl;
  } else if (T == 2) {
    memset(memo, -1, sizeof(memo));
    cout << ans(0, -1) << endl;
  }

  return 0;
}
