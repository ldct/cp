#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

struct UF {
  vector<int> e;
  UF(int n) : e(n, -1) {}
  bool sameSet(int a, int b) { return find(a) == find(b); }
  int size(int x) { return -e[find(x)]; }
  int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
  bool join(int a, int b) {
    a = find(a), b = find(b);
    if (a == b) return false;
    if (e[a] > e[b]) swap(a, b);
    e[a] += e[b]; e[b] = a;
    return true;
  }
};

int N, M;
int F[100009];
vector<pair<int, int>> edges;

int main() {

  cin >> N >> M;

  for (int i=0; i<N; i++) cin >> F[i];

  for (int i=0; i<N-1; i++) {
    pair<int, int> p = {F[i+1] - F[i], i};
    edges.push_back(p);
  }

  sort(edges.begin(), edges.end());

  // cout << "edges=" << edges << endl;

  UF uf(N);

  for (int i=0; i<M; i++) {
    int x, y;
    cin >> x >> y;
    x--; y--;
    uf.join(x, y);
  }

  long long ret = 0;

  for (const auto p : edges) {
    int a = p.second;
    int b = a + 1;

    if (uf.sameSet(a, b)) continue;
    uf.join(a, b);
    ret += (long long)(F[b] - F[a]);
  }

  cout << ret << endl;

  return 0;
}
