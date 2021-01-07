#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

constexpr size_t MAX_N = 200009;

int N, Q;

vector<int> neighbours[MAX_N];
int depth[MAX_N];
pair<int, int> edges[MAX_N];
long long lazy[MAX_N];

void dfs1(int u, int daddy, int curr_depth) {
  depth[u] = curr_depth;
  for (int v : neighbours[u]) {
    if (v == daddy) continue;
    dfs1(v, u, curr_depth+1);
  }
}

void dfs2(int u, int daddy) {
  for (int v : neighbours[u]) {
    if (v == daddy) continue;
    lazy[v] += lazy[u];
    dfs2(v, u);
  }
}

int main() {

  memset(lazy, 0, sizeof(lazy));

  cin >> N;

  for (int i=0; i<N-1; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    neighbours[a].push_back(b);
    neighbours[b].push_back(a);
    edges[i] = {a, b};
  }

  dfs1(0, -1, 0);

  cin >> Q;

  for (int q=0; q<Q; q++) {
    long long t, e, x;
    cin >> t >> e >> x;
    e--;
    assert(t ==  1 || t == 2);
    int a, b;
    a = edges[e].first;
    b = edges[e].second;
    if (t == 2) {
      swap(a, b);
    }
    int d_depth = depth[a] - depth[b];
    assert(d_depth == -1 || d_depth == 1);

    if (depth[a] < depth[b]) {
      // cout << "query #" << (q+1) << " contributes " << x << " to the root" << endl;
      lazy[0] += x;
      lazy[b] -= x;
    } else {
      if (a == 0) {
        // cout << "query #" << (q+1) << " contributes " << x << " to the root" << endl;
      }
      lazy[a] += x;
    }
  }

  dfs2(0, -1);

  for (int i=0; i<N; i++) {
    cout << lazy[i] << endl;
  }

  return 0;
}
