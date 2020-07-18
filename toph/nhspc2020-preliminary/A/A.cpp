#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

constexpr size_t MAX_N = 100009;

int N,Q,R;
long long values[MAX_N];
vector<int> neighbours[MAX_N];
vector<int> children[MAX_N];
int depth[MAX_N];

void dfs(int parent, int v, int d) {
  depth[v] = d;
  for (int u : neighbours[v]) {
    if (u != parent) {
      children[v].push_back(u);
      dfs(v, u, d+1);
    }
  }
}

int main() {
  
  int T;

  cin >> T;

  while (T --> 0) {
    cin >> N >> Q >> R;

    for (int i=1; i<=N; i++) {
      neighbours[i].clear();
      children[i].clear();
      cin >> values[i];
    }
    for (int i=0; i<N-1; i++) {
      int u, v;
      cin >> u >> v;
      neighbours[u].push_back(v);
      neighbours[v].push_back(u);
    }

    dfs(R, R, 0);

    // for (int i=1; i<=N; i++) {
    //   cout << "children[" << i << "]=" << children[i] << endl;
    // }

    for (int i=0; i<Q; i++) {
      int u, k;
      cin >> u >> k;
    }
  }
    
  return 0;
}
