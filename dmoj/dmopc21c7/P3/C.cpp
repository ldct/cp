#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define i32 int32_t

constexpr int MAX_N = 1000009;

vector<int> old_children[MAX_N];
int num_children[MAX_N];
vector<int> parents[MAX_N];

vector<int> state;
vector<int> lazy_flip;

stack<int> sinks;
vector<int> toposort;

int N, M;

void clear_sink(int u) {
  for (auto p : parents[u]) {
    num_children[p]--;
    if (num_children[p] == 0) {
      sinks.push(p);
    }
  }
}

i32 main() {

  ios_base::sync_with_stdio(false); cin.tie(NULL);
  memset(num_children, 0, sizeof(num_children));

  cin >> N >> M;

  state.push_back(-1); lazy_flip.push_back(-1);

  for (int i=0; i<N; i++) {
    int x;
    cin >> x;
    state.push_back(x);
    lazy_flip.push_back(0);
  }
  for (int i=0; i<M; i++) {
    int a, b;
    cin >> a >> b;
    num_children[a]++; old_children[a].push_back(b);
    parents[b].push_back(a);
  }

  for (int i=1; i<=N; i++) {
    if (num_children[i] == 0) sinks.push(i);
  }

  while (sinks.size()) {
    auto s = sinks.top();
    toposort.push_back(s);
    sinks.pop();
    clear_sink(s);
  }

  auto in_ts = vector<int>(N+1, 0);
  for (auto u : toposort) {
    in_ts[u] = 1;
  }

  for (int i=1; i<=N; i++) {
    if (!in_ts[i] && state[i] == 1) {
      cout << -1 << endl;
      return 0;
    }
  }

  reverse(toposort.begin(), toposort.end());

  int ret = 0;

  for (auto u : toposort) {
    for (auto v : old_children[u]) {
      lazy_flip[v] += lazy_flip[u];
      lazy_flip[v] = lazy_flip[v] % 2;
    }
    if (lazy_flip[u] % 2 == 1) {
      state[u] = 1 - state[u];
    }
    if (state[u] == 1) {
      ret++;
      // cout << "flip " << u << endl;
      for (auto v : old_children[u]) {
        lazy_flip[v]++;
        lazy_flip[v] = lazy_flip[v] % 2;
      }
      // cout << lazy_flip << endl;
    }
  }

  cout << ret << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS