#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

int N;
vector<pair<long long, long long>> neighbours[200009];
vector<long long> ett;
constexpr long long MODULUS = 10000007;

void dfs(int u, int parent) {
  for (auto p : neighbours[u]) {
    int v = p.first;
    long long w = p.second;
    if (v == parent) continue;
    ett.push_back(w);
    dfs(v, u);
    ett.push_back(w);
  }
}

int main() {

  cin >> N;

  for (int i=0; i<N-1; i++) {
    long long u, v, w;
    cin >> u >> v >> w;
    u--; v--;
    neighbours[u].push_back({v, w});
    neighbours[v].push_back({u, w});
  }

  dfs(0, -1);

  cout << ett << endl;

  long long ret = 0;

  for (int i=0; i<ett.size(); i++) {
    for (int j=i+2;j<ett.size(); j++) {
      // calculate [i,j]
      long long contribution = 0;
      for (int k=i; k<=j; k++) {
        contribution ^= ett[k];
      }
      cout << "contribution=" << contribution << endl;
      contribution %= MODULUS;
      ret += contribution;
      ret %= MODULUS;
    }
  }

  cout << ret << endl;

  return 0;
}
