#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

constexpr int MAX_N = 100009;

int N;
vector<int> children[MAX_N];
int subtree_size[MAX_N];

void dfs1(int u) {
  subtree_size[u] = 1;
  for (const auto v : children[u]) {
    dfs1(v);
    subtree_size[u] += subtree_size[v];
  }
}

int dfs2(int u) {
  if (children[u].size() == 0) return -1;

  vector<int> is;
  vector<int> ns;

  int ret = -1;
  for (const auto v : children[u]) {
    if (subtree_size[v] % 2 == 1) {
      is.push_back(dfs2(v));
    } else {
      ns.push_back(dfs2(v));
    }
  }

  sort(is.begin(), is.end());
  reverse(is.begin(), is.end());

  for (int i=0; i<ns.size(); i++) {
    if (ns[i] > 0) ret += ns[i];
  }

  int m = 1;

  for (int i=0; i<is.size(); i++) {
    ret += m*is[i];
    m *= -1;
  }

  for (int i=0; i<ns.size(); i++) {
    if (ns[i] < 0) ret += m*ns[i];
  }

  if (false && u == 0) {
    cout << "is = " << is << endl;
    cout << "ns = " << ns << endl;
    cout << "ret = " << ret << endl;
  }

  return ret;

}

int main() {

  cin >> N;

  for (int i=1; i<N; i++) {
    int p;
    cin >> p;
    p--;
    children[p].push_back(i);
  }

  dfs1(0);

  int k = dfs2(0);
  k = -k;
  // cout << k << endl;
  cout << ((k + N) / 2)  << endl;

  // for (int i=0; i<N; i++) {
  //   cout << subtree_size[i] << endl;
  // }




  return 0;
}
