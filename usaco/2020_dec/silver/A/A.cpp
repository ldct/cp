#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

constexpr size_t MAX_N = 100009;
int N;
vector<int> neighbours[MAX_N];

long long ans(int parent, int u) {

  long long ret = 0;
  long long num_children = 0;

  for (auto v : neighbours[u]) {
    if (parent == v) continue;
    num_children++;
    ret += ans(u, v);
  }

  if (num_children > 0) {
    ret += num_children;
    ret += ceil(log2(num_children + 1));
  }

  return ret;
}

int main() {

  cin >> N;

  for (int i=0; i<N-1; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    neighbours[a].push_back(b);
    neighbours[b].push_back(a);
  }

  // for (int u=0; u<N; u++) {
  //   cout << "u=" << u << "neighbours[u]=" << neighbours[u] << endl;
  // }

  cout << ans(-1, 0) << endl;

  return 0;
}
