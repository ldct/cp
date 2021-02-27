#include <bits/stdc++.h>
using namespace std;

template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

constexpr size_t MAX_N = 2000009;

int N, W, D;

vector<int> neighbours[MAX_N];
bool visited[MAX_N];
int d[MAX_N];

void bfs() {

  memset(visited, 0, sizeof(visited));
  for (int i=0; i<N; i++) d[i] = MAX_N;

  queue<int> q;

  q.push(N-1);
  visited[N-1] = true;
  d[N-1] = 0;
  while (!q.empty()) {
    int v = q.front(); q.pop();
    for (int u : neighbours[v]) {
      if (!visited[u]) {
        visited[u] = true;
        q.push(u);
        d[u] = d[v] + 1;
      }
    }
  }
}

int P[MAX_N];
int cost[MAX_N];

int main() {

  cin >> N >> W >> D;
  for (int i=0; i<W; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    neighbours[b].push_back(a);
  }

  bfs();

  for (int i=0; i<N; i++) {
    cin >> P[i];
    P[i]--;
  }

  for (int i=0; i<N; i++) { cost[i] = i + d[P[i]]; }
  multiset<int> C;
  for (int i=0; i<N; i++) { C.insert(i + d[P[i]]); }
  // cout << C << endl;
  // for (int i=0; i<N; i++) { cout << cost[i] << " "; } cout << endl;

  for (int i=0; i<D; i++) {
    int x, y;
    cin >> x >> y;
    x--; y--;
    swap(P[x], P[y]);
    C.erase(C.find(cost[x])); C.erase(C.find(cost[y]));
    cost[x] = x + d[P[x]]; C.insert(x + d[P[x]]);
    cost[y] = y + d[P[y]]; C.insert(y + d[P[y]]);

    cout << (*C.begin()) << endl;

    // for (int i=0; i<N; i++) {
    //   assert(cost[i] == i + d[P[i]]);
    // }
    // int ret = MAX_N; for (int i=0; i<N; i++) { ret = min(ret, cost[i]); } cout << ret << endl;

    // for (int i=0; i<N; i++) { cout << cost[i] << " "; } cout << endl;


  }



  return 0;
}
