#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

constexpr size_t MAX_N = 100009;

long long N, M;
long long P[MAX_N];
long long H[MAX_N];

vector<int> neighbours[MAX_N];

pair<long long, long long> dfs(int parent, int u) {
  vector<int> children;
  for (const auto v : neighbours[u]) {
    if (v != parent) children.push_back(v);
  }
  if (children.size() == 0) {
    long long st_pop = P[u];
    long long two_h = st_pop + H[u];
    if (two_h % 2 != 0) {
      return {-1, -1};
    }
    long long happy = two_h / 2;
    long long unhappy = st_pop - happy;
    if (happy - unhappy != H[u]) {
      return {-1, -1};
    }
    if (happy < 0 || unhappy < 0) {
      return {-1, -1};
    }
    return {happy, unhappy};
  } else {
    long long st_pop = P[u];

    vector<pair<long long, long long>> res;

    for (const auto v : children) {
      auto p = dfs(u, v);
      if (p.first == -1) return {-1, -1};
      res.push_back(p);
      st_pop += (p.first + p.second);
    }

    long long two_h = st_pop + H[u];
    if (two_h % 2 != 0) {
      return {-1, -1};
    }
    long long happy = two_h / 2;
    long long unhappy = st_pop - happy;
    if (happy - unhappy != H[u]) {
      return {-1, -1};
    }

    if (happy < 0 || unhappy < 0) {
      return {-1, -1};
    }

    pair<long long, long long> ret = { happy, unhappy };

    for (auto p : res) {
      happy -= p.first;
      if (happy < 0) {
        return {-1, -1};
      }
    }

    unhappy += happy;
    happy = 0;

    // cout << "sending " << unhappy << "to " << res << endl;
    for (auto p : res) {
      unhappy -= p.second;
      if (unhappy < 0) {
        return {-1, -1};
      }
    }

    return ret;
  }
}

int main() {
  
  int T;
  cin >> T;
  
  while (T --> 0) {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
      neighbours[i].clear();
    }
    for (int i=0; i<N; i++) {
      cin >> P[i];
    }
    for (int i=0; i<N; i++) {
      cin >> H[i];
    }
    for (int i=0; i<N-1; i++) {
      int x, y;
      cin >> x >> y;
      x--; y--;
      neighbours[x].push_back(y);
      neighbours[y].push_back(x);
    }
    if (dfs(0, 0).first == -1) {
      cout << "NO" << endl;
    } else {
      cout << "YES" << endl;
    }
  }
    
  return 0;
}
