#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

int N, M;

vector<pair<int, int>> adj[200009];

void dijkstra(int s, vector<int>& d, vector<int> & p) {
  d.assign(N, LLONG_MAX);
  p.assign(N, -1);

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
            p[to] = v;
            q.push({d[to], to});
        }
    }
  }
}
i32 main() {

  cin >> N >> M;
  for (int i=0; i<M; i++) {
    int a, b, w;
    cin >> a >> b >> w;
    a--; b--;
    adj[a].push_back({b, w});
    adj[b].push_back({a, w});
  }

  vector<int> d, p;
  dijkstra(0, d, p);

  if (d[N-1] == LLONG_MAX) {
    cout << -1 << endl;
    return 0;
  }

  vector<int> ret;
  ret.push_back(N-1);

  while (ret[ret.size()-1] != 0) {
    ret.push_back(p[ret[ret.size()-1]]);
  }

  reverse(ret.begin(), ret.end());

  for (auto r : ret) {
    cout << (1+r) << " ";
  }
  cout << endl;

  return 0;
}
