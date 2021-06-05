#include <bits/stdc++.h>
using namespace std;

#define int long long

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

int Q;
int amount[300009];
int cost[300009];
bool depleted[300009];
int parent[300009];
int memo[300009][19];
int depth[300009];

int pow_parent(int u, int k) {
  // the 2^kth parent of u
  if (memo[u][k] != -1) return memo[u][k];
  if (k == 0) return parent[u];
  return memo[u][k] = pow_parent(pow_parent(u, k-1), k-1);
}

int kth_parent(int u, int k) {
  if (k == 0) return u;
  // the kth parent of u
  int p = 0;
  while ((1 << (p+1)) <= k) p++;
  return kth_parent(pow_parent(u, p), k-(1<<p));
}

int search(int depth, int v) {
  // reduce depth while avoiding too many depleted

  int low=0, high=depth;

  if (depleted[kth_parent(v, low)]) return low;
  if (!depleted[kth_parent(v, high)]) return high;

  while (high - low > 3) {
    assert(!depleted[kth_parent(v, low)]);
    assert(depleted[kth_parent(v, high)]);

    int mid = (low + high) / 2;
    if (depleted[kth_parent(v, mid)]) {
      high = mid;
    } else {
      low = mid;
    }
  }

  return high;

}

int32_t main() {

  depth[0] = 0;

  memset(depleted, 0, sizeof(depleted));
  memset(memo, -1, sizeof(memo));

  cin >> Q >> amount[0] >> cost[0];

  for (int i=1; i<=Q; i++) {
    int t;
    cin >> t;
    if (t == 1) {
      cin >> parent[i] >> amount[i] >> cost[i];
      depth[i] = depth[parent[i]] + 1;
    } else if (t == 2) {
      int v, w;
      cin >> v >> w;

      int curr_depth = depth[v];
      assert(kth_parent(v, curr_depth) == 0);

      curr_depth = search(curr_depth, v);

      int bought = 0;
      int spent = 0;
      while (curr_depth >= 0 && bought < w) {
        int curr_node = kth_parent(v, curr_depth);
        int this_buy = min(amount[curr_node], (w - bought));

        amount[curr_node] -= this_buy;
        if (amount[curr_node] == 0) depleted[curr_node] = true;
        bought += this_buy;

        spent += this_buy*cost[curr_node];

        curr_depth--;
      }
      cout << bought << " " << spent << endl;
    } else {
      assert(false);
    }
  }

  return 0;
}
