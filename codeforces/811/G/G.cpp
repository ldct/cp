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

constexpr int MAX_N = 200009;
int N;
vector<int> children[MAX_N];

int A[MAX_N];
int B[MAX_N];
int ANS[MAX_N];

int CURRENT_WEIGHT = 0;
vector<int> CURRENT_PREFIX = {0};


void dfs(int u) {
  auto i = lower_bound(CURRENT_PREFIX.begin(), CURRENT_PREFIX.end(), CURRENT_WEIGHT+1) - CURRENT_PREFIX.begin();
  ANS[u] = i;

  if (u == -5) {
    cout << CURRENT_WEIGHT << CURRENT_PREFIX << endl;
  }

  for (auto v : children[u]) {
    CURRENT_WEIGHT += A[v];
    CURRENT_PREFIX.push_back(B[v] + CURRENT_PREFIX[CURRENT_PREFIX.size() - 1]);
    dfs(v);
    CURRENT_WEIGHT -= A[v];
    CURRENT_PREFIX.pop_back();
  }
}

i32 main() {

  int T;
  cin >> T;

  while (T --> 0) {
    cin >> N;
    for (int i=1; i<=N; i++) {
      children[i].clear();
    }
    for (int i=2; i<=N; i++) {
      int p;
      cin >> p >> A[i] >> B[i];
      children[p].push_back(i);
    }
    dfs(1);

    for (int i=2; i<=N; i++) {
      cout << (ANS[i] - 1) << " ";
    }
    cout << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS