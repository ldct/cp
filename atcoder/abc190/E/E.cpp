#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

constexpr int MAX_N = 100009;
int N, M, K;

vector<int> neighbours[MAX_N];
vector<int> C;
map<int, int> C_i;

long long memo[1 << 19][19];

long long fastest[19][19];

void bfs(int si) {

  int s = C[si];

  queue<int> q;
  vector<bool> used(N+1, 0);
  vector<int> d(N+1, 0);

  q.push(s);
  used[s] = true;
  while (!q.empty()) {
    int v = q.front();
    q.pop();
    for (int u : neighbours[v]) {
      if (!used[u]) {
          used[u] = true;
          q.push(u);
          d[u] = d[v] + 1;
          if (C_i.find(u) != C_i.end()) {
            fastest[si][C_i[u]] = fastest[C_i[u]][si] = d[u];
          }
      }
    }
  }
}

long long ans(unsigned mask, int j) {
  if (__builtin_popcount(mask) == 0) return 1;

  if (memo[mask][j] != -1) return memo[mask][j];

  long long ret = LLONG_MAX;

  for (int i=0; i<K; i++) {
    if (0 == (mask & (1 << i))) continue;
    long long candidate = fastest[j][i] + ans(mask & ~(1 << i), i);
    ret = min(ret, candidate);
  }
  return memo[mask][j] = ret;
}

int main() {

  memset(fastest, -1, sizeof(fastest));

  cin >> N >> M;

  for (int i=0; i<M; i++) {
    int a, b;
    cin >> a >> b;
    neighbours[a].push_back(b);
    neighbours[b].push_back(a);
  }

  cin >> K;
  for (int i=0; i<K; i++) {
    int c;
    cin >> c;
    C.push_back(c);
    C_i[c] = i;
  }

  for (int i=0; i<(1<<K); i++) {
    for (int j=0; j<K; j++) {
      memo[i][j] = -1;
    }
  }

  for (int i=0; i<K; i++) bfs(i);

  for (int i=0; i<K; i++) for (int j=0; j<K; j++) if ((i != j) && fastest[i][j] == -1) {
    cout << -1 << endl;
    return 0;
  }

  // for (int i=0; i<K; i++) {
  //   for (int j=0; j<K; j++) {
  //     cout << fastest[i][j] << " ";
  //   }
  //   cout << endl;
  // }
  // return 0;

  long long ret = LLONG_MAX;
  for (int j = 0; j<K; j++) {
    int mask = (1 << K) - 1;
    mask &= ~(1 << j);
    ret = min(ret, ans(mask, j));
  }
  cout << ret << endl;

  return 0;
}
