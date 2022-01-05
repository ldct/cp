#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

const int dx[4] = {1,0,-1,0}, dy[4] = {0,1,0,-1};

int N;
int costs[509][509];
int ret;

const int INF = LLONG_MAX;
vector<pair<int, int>> adj[250009];

int vertex(int x, int y) {
  return 2*N*x + y;
}

void dijkstra(int s, vector<int>& d) {
  d.assign(4*N*N, INF);

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
        int to = edge.first;
        int len = edge.second;

        if (d[v] + len < d[to]) {
            d[to] = d[v] + len;
            q.push({d[to], to});
        }
    }
  }
}

i32 main() {

  int T;
  cin >> T;
  while (T --> 0) {

    ret = 0;

    cin >> N;
    for (int i=0; i<4*N*N; i++) adj[i].clear();

    for (int i=0; i<2*N; i++) for (int j=0; j<2*N; j++) {
      cin >> costs[i][j];
    if (
      (i >= N && j >= N)
     ) {
       ret += costs[i][j];
       costs[i][j] = 0;
     }
    }

    for (int x=0; x<2*N; x++) for (int y=0; y<2*N; y++) {
      int u = vertex(x, y);

      for(int i = 0; i < 4; i++) {
        auto newX = x + dx[i]; auto newY = y + dy[i];
        newX += 2*N; newX %= (2*N);
        newY += 2*N; newY %= (2*N);

        int v = vertex(newX, newY);

        adj[u].push_back({v, costs[newX][newY]});
        adj[v].push_back({u, costs[x][y]});

        // adj[u].push_back({v, 1});
        // adj[v].push_back({u, 1});
      }
    }

    vector<int> d;
    dijkstra(0, d);


    cout << d[4*N*N-1] + ret << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS