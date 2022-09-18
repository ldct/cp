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

constexpr size_t MAX_N = 200009;

int N;
vector<int> neighbours[MAX_N];
int max_depth;
int depth_of[MAX_N];

typedef struct _Query {
  int idx;
  int node;
  int dist;
  int ans;
} Query;

vector<int> diameter;
bool in_diameter[MAX_N];
vector<Query> queries[MAX_N];
int diameter_idx;

// label each node by its depth
void dfs(int u, int parent, int depth) {
  depth_of[u] = depth;
  max_depth = max(max_depth, depth);
  for (const auto& v : neighbours[u]) {
    if (v == parent) continue;
    dfs(v, u, depth+1);
  }
}
 
// mark the diameter; call it from the deepest node
void dfs_mark(int u) {
  diameter.push_back(u);
  in_diameter[u] = true;
  auto d = depth_of[u];
  for (const auto& v : neighbours[u]) {
    if (depth_of[v] == d-1) {
      dfs_mark(v);
      return;
    }
  }
}

void dfs_solve(int u, int parent, vector<int>& ancestors) {

  for (auto& q : queries[u]) {
    if (q.dist < ancestors.size()) {
      q.ans = ancestors[ancestors.size()-1-q.dist];
    } else {
      int rem = q.dist - ancestors.size();
      int a = diameter_idx - rem;
      int b = diameter_idx + rem;

      if (0 <= a && a < diameter.size()) q.ans = diameter[a];
      if (0 <= b && b < diameter.size()) q.ans = diameter[b];
    }
  }

  for (const auto& v : neighbours[u]) {
    if (v == parent) continue;
    if (in_diameter[v]) continue;
    ancestors.push_back(v);
    dfs_solve(v, u, ancestors);
    ancestors.pop_back();
  }
}

i32 main() {

  memset(in_diameter, 0, sizeof(in_diameter));
  
  cin >> N;
  for (int i=0; i<N-1; i++) {
    int a, b;
    cin >> a >> b;
    neighbours[a].push_back(b);
    neighbours[b].push_back(a);
  }
  int Q;
  cin >> Q;
  for (int i=0; i<Q; i++) {
    int u, k;
    cin >> u >> k;
    
    Query q;
    q.idx = i; q.node = u; q.dist = k; q.ans = -1;
    
    queries[u].push_back(q);
  }

  max_depth = -1;
  dfs(1, 1, 0);

  int new_root;
  for (int i=1; i<=N; i++) {
    if (depth_of[i] == max_depth) {
      new_root = i;
    }
  }

  dfs(new_root, new_root, 0);

  for (int i=1; i<=N; i++) {
    if (depth_of[i] == max_depth) {
      new_root = i;
    }
  }

  dfs_mark(new_root);

  // cout << diameter << endl;

  vector<int> ancestors;

  for (diameter_idx=0; diameter_idx<diameter.size(); diameter_idx++) {
    int u = diameter[diameter_idx];
    dfs_solve(u, u, ancestors);
  }

  vector<pair<int, int>> ret;

  for (int i=1; i<=N; i++) {
    for (auto q : queries[i]) {
      ret.push_back({q.idx, q.ans});
    }
  }

  sort(ret.begin(), ret.end());

  for (auto r : ret) {
    cout << r.second << endl;
  }
    
  return 0;
}
