vector<pair<long long, long long>> adj[100009];

void dijkstra(long long N, long long s, vector<long long>& d, bool reverse) {
  d.assign(N, LLONG_MAX);

  using pii = pair<long long, long long>;
  priority_queue<pii, vector<pii>, greater<pii>> q;

  d[s] = 0;
  q.push({0, s});

  while (!q.empty()) {
    long long v = q.top().second;
    long long d_v = q.top().first;
    q.pop();
    if (d_v != d[v])
        continue;

    for (auto edge : adj[v]) {
        long long to = edge.first;
        long long len = edge.second;

        if (d[v] + len < d[to]) {
            d[to] = d[v] + len;
            q.push({d[to], to});
        }
    }
}

  }
