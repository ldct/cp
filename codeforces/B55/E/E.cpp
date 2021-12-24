#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

int N, M, K;
vector<int> adj[3009];
unordered_set<int> forbidden[3009][3009];

constexpr int INF = 200009;

void dijkstra(int s, vector<int>& d) {
  d.assign(N, INF);

  using pii = pair<int, int>;
  priority_queue<pii, vector<pii>, greater<pii>> q;

  d[s] = 0;
  q.push({0, s});

  while (!q.empty()) {
    int v = q.top().second;
    int d_v = q.top().first;
    q.pop();
    if (d_v != d[v])
        continue;

    for (auto edge : adj[v]) {
        int to = edge;
        int len = 1;

        if (d[v] + len < d[to]) {
            d[to] = d[v] + len;
            q.push({d[to], to});
        }
    }
  }
}
i32 main() {

  cin >> N >> M >> K;
  for (int i=0; i<M; i++) {
    int x, y;
    cin >> x >> y;
    x--; y--;
    adj[x].push_back(y);
    adj[y].push_back(x);
  }

  for (int i=0; i<K; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    a--; b--; c--;
    forbidden[a][b].insert(c);
  }

  cout << N << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS