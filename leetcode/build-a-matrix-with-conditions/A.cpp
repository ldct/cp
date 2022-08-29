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

int N;
constexpr size_t MAX_N = 10009;
vector<int> neighbours[MAX_N];
vector<int> toposort_ans;
int visited[MAX_N];
bool has_cycle;

void dfs(int daddy, int v) {
  visited[v] = 0;
  for (int u : neighbours[v]) {
    if (visited[u] == 0) has_cycle = true;
    if (visited[u] == -1) dfs(daddy, u);
  }
  visited[v] = daddy;
  toposort_ans.push_back(v);
}

void topological_sort() {
  for (int i = 1; i <= N; ++i) {
    if (visited[i] == -1) dfs(i, i);
  }
  reverse(toposort_ans.begin(), toposort_ans.end());
}

class Solution {
public:
    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {

      vector<vector<int>> ret;
      has_cycle = 0;

      for (int i=0; i<k; i++) {
        ret.push_back(vector<int>(k, 0));
      }

      N = k;
      for (int i=1; i<=N; i++) {
        neighbours[i].clear();
        visited[i] = -1;
      }
      for (auto r : rowConditions) {
        neighbours[r[0]].push_back(r[1]);
      }

      topological_sort();
      if (has_cycle) return {};

      vector<int> row_order = toposort_ans;

      toposort_ans.clear();
      has_cycle = 0;

      for (int i=1; i<=N; i++) {
        neighbours[i].clear();
        visited[i] = -1;
      }
      for (auto r : colConditions) {
        neighbours[r[0]].push_back(r[1]);
      }
      topological_sort();
      if (has_cycle) return {};

      cout << row_order << toposort_ans << endl;

      for (int i=0; i<k; i++) {
        int e = row_order[i];
        int j = 0;
        for (j=0; j<k; j++) if (toposort_ans[j] == e) break;
        ret[i][j] = e;
      }


      return ret;
    }
};

i32 main() {

  vector<vector<int>> r = {{1,2},{7,3},{4,3},{5,8},{7,8},{8,2},{5,8},{3,2},{1,3},{7,6},{4,3},{7,4},{4,8},{7,3},{7,5}};
  vector<vector<int>> c = {{5,7},{2,7},{4,3},{6,7},{4,3},{2,3},{6,2}};

  auto s = Solution();
  cout << s.buildMatrix(8, r, c) << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS