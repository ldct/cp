#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

constexpr size_t MAX_N = 300009;

int N;
vector<int> neighbours[MAX_N];
int subtree_size[MAX_N];

int dfs(int u, int parent) {
  for (const auto v : neighbours[u]) {
    if (v == parent) continue;
    subtree_size[u] += dfs(v, u);
  }
  subtree_size[u] += 1;
  return subtree_size[u];
}

pair<int, int> centroid(int u, int p) {
  for (const auto v : neighbours[u])
    if (v != p && subtree_size[v] > N/2) return centroid(v, u);

  return {u, p};
}

pair<int, int> leaf(int u, int p) {
  for (const auto v : neighbours[u]) if (v != p) return leaf(v, u);
  return {u, p};
}

int uu, vv;

int main() {
  
  int T;
  cin >> T;

  while (T --> 0) {
    cin >> N;
    for (int i=0; i<N; i++) {
      neighbours[i].clear();
      subtree_size[i] = 0;
    }

    for (int i=0; i<N-1; i++) {
      cin >> uu >> vv;
      uu--; vv--;
      neighbours[uu].push_back(vv);
      neighbours[vv].push_back(uu);
    }


    dfs(0, -1);
    auto p = centroid(0, -1);
    int c1 = p.first;
    int cp = p.second;

    int c2 = -1;
    for (const auto v : neighbours[c1]) {
      if (v == cp) continue;
      if (subtree_size[v] == N/2) {
        c2 = v;
      }
    }

    if (c2 == -1) {
      uu++; vv++;
      cout << uu << " " << vv << endl;
      cout << uu << " " << vv << endl;
      continue;
    }

    // disconnect the leaf
    auto p2 = leaf(c2, c1);
    cout << (p2.first + 1) << " " << (p2.second + 1) << endl;
    // attach the leaf to c1
    cout << (c1 + 1) << " " << (p2.first + 1) << endl;
  }
    
  return 0;
}
