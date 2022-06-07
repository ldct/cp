#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int N, M, Q;
vector<int> neighbours[3009];
int d[3009][3009];

void query(int s, int t, int x, int u, int v, int y) {
  if (d[s][t] <= x) {
    cout << "YES" << endl;
    return;
  }
  if (d[u][v] <= y) {
    cout << "YES" << endl;
    return;
  }
  if (d[s][u] + d[t][v] + 2 <= x + y) {
    cout << "YES" << endl;
    return;
  }
  if (d[s][v] + d[t][u] + 2 <= x + y) {
    cout << "YES" << endl;
    return;
  }

  cout << "NO" << endl;
}

i32 main() {

  ios_base::sync_with_stdio(false); cin.tie(NULL);

  memset(d, 0, sizeof(d));

  cin >> N >> M;
  for (int i=0; i<M; i++) {
    int a, b;
    cin >> a >> b;
    neighbours[a].push_back(b);
    neighbours[b].push_back(a);
  }

  for (int s=1; s<=N; s++) {

    queue<int> q;
    vector<bool> used(N);

    q.push(s);
    used[s] = true;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int u : neighbours[v]) {
            if (!used[u]) {
                used[u] = true;
                q.push(u);
                d[s][u] = d[s][v] + 1;
            }
        }
    }
  }


  cin >> Q;

  while (Q --> 0) {
    int s, t, x, u, v, y;
    cin >> s >> t >> x >> u >> v >> y;
    query(s, t, x, u, v, y);
  }


  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS