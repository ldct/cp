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

constexpr int MAX_N = 100009;

int N, K;

vector<int> children[MAX_N];
int ans[MAX_N];

typedef struct _ap2 {
  // -1 -> invalid
  // 0 -> even
  // 1 -> odd
  // 2 -> infinite
  int kind;
  int left, right;
  void pprint() {
    if (kind == 2) {
      cout << "inf" << endl;
      return;
    }
    if (kind == -1) {
      cout << "{}" << endl;
      return;
    }
    cout << "k=" << kind << "[" << left << "," << right << "]" << endl;
  }
} ap2;

ap2 make(int k, int l, int r) {
  ap2 ret;
  ret.kind = k;
  ret.left = l;
  ret.right = r;
  return ret;
}

ap2 single(int x) {
  return make(
    x%2, x, x
  );
}

ap2 merge(ap2 lhs, ap2 rhs) {
  if (lhs.kind == -1) return lhs;
  if (rhs.kind == -1) return rhs;
  if (lhs.kind == 2) return rhs;
  if (rhs.kind == 2) return lhs;
  if (lhs.kind != rhs.kind) return make(-1, -1, -1);
  int l = max(lhs.left, rhs.left);
  int r = min(lhs.right, rhs.right);

  if (!(l <= r)) return make(-1, -1, -1);
  return make(lhs.kind, l, r);
}

ap2 flip(ap2 a) {
  if (a.kind == -1 || a.kind == 2) return a;
  return make(1-a.kind, a.left-1, a.right+1);
}

ap2 dfs(int u, int parent) {
  
  ap2 ret = make(2, -1, -1);
  if (ans[u] != -1) ret = single(ans[u]);

  for (auto v : children[u]) {
    if (v == parent) continue;
    ret = merge(ret, flip(dfs(v, u)));
  }
  return ret;
}

i32 main() {

  memset(ans, -1, sizeof(ans));

  cin >> N;
  for (int i=0; i<N-1; i++) {
    int a, b;
    cin >> a >> b;
    children[a].push_back(b);
    children[b].push_back(a);
  }
  cin >> K;
  for (int i=0; i<K; i++) {
    int v, p;
    cin >> v >> p;
    ans[v] = p;
  }

  auto r = dfs(1, 1);
  r.pprint();

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS