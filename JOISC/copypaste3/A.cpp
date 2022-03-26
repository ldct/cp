#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

string ALPHABET = "abcdefghijklmnopqrstuvwxyz";

int N, A, B, C;
string S;
map<string, int> string_idx;
set<string> strings;
int num_substrings = 0;
vector<pair<int, int>> adj[6250000];


void dijkstra(long long N, long long s, vector<long long>& d) {
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

int pair_idx(string x, string y) {
  return string_idx[x] * num_substrings + string_idx[y];
}

void add_edge(string a, string b, string c, string d, int w) {
  adj[pair_idx(a, b)].push_back({pair_idx(c, d), w});
}

i32 main() {

  cin >> N >> S >> A >> B >> C;

  for (int i=0; i<S.size(); i++) {
    for (int j=i; j<S.size()+1; j++) {
      string s = S.substr(i, j);
      if (string_idx.count(s)) {
        continue;
      } else {
        string_idx[s] = num_substrings++;
        strings.insert(s);
      }
    }
  }

  assert(num_substrings == strings.size());

  for (auto X : strings) {
    for (auto Y : strings) {

      for (char c : ALPHABET) {
        if (strings.count(X + c)) {
          add_edge(X, Y, X+c, Y, A);
        }
      }
      add_edge(X, Y, "", X, B);

      if (strings.count(X+Y)) {
        add_edge(X, Y, X+Y, Y, C);
      }
    }

  }

  vector<int> d;

  dijkstra(num_substrings*num_substrings, pair_idx("", ""), d);


  int ret = LLONG_MAX;

  for (auto Y : strings) {
    ret = min(ret, d[pair_idx(S, Y)]);
  }

  cout << ret << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS