#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

constexpr size_t MAX_N = 2000009;

using iii = int;

#define int long long

int N,M,T;

vector<pair<int,int>> all_edges;
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

iii main() {
  
  cin >> T;

  while (T --> 0) {
    all_edges.clear();
    toposort_ans.clear();
    has_cycle = false;
    cin >> N >> M;
    for (int i=1; i<=N; i++) {
      neighbours[i].clear();
      visited[i] = -1;
    }
    for (int i=0; i<M; i++) {
      int t,x,y;
      cin >> t >> x >> y;
      all_edges.push_back(make_pair(x, y));
      if (t == 1) {
        neighbours[x].push_back(y);
      } else {
        assert(t == 0);
      }
    }
    // toposort
    topological_sort();

    if (has_cycle) {
      cout << "NO" << endl;
    } else {
      cout << "YES" << endl;

      // cout << "sort=" << toposort_ans << endl;

      auto level_of = vector<int>(N+1, -1);

      assert(toposort_ans.size() == N);

      for (int i=0; i<toposort_ans.size(); i++) {
        level_of[toposort_ans[i]] = i;
      }

      assert(all_edges.size() == M);
      for (const auto& p : all_edges) {
        auto x = p.first;
        auto y = p.second;

        assert(1 <= x && x <= N);
        assert(1 <= y && y <= N);
        assert(level_of[x] != -1);
        assert(level_of[y] != -1);
        assert(level_of[x] != level_of[y]);

        if (level_of[x] > level_of[y]) {
          cout << y << " " << x << endl;
        } else {
          cout << x << " " << y << endl;
        }
      }
      sort(toposort_ans.begin(), toposort_ans.end());
      for (int i=0; i<toposort_ans.size(); i++) {
        assert(toposort_ans[i] == i+1);
      }
    }
  }    
  return 0;
}
