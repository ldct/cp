#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

template<typename T>
class PQ_del { /* max priority queue with deletion */
public:
  priority_queue<T> pq;
  priority_queue<T> deleted;

  T top() { return pq.top(); }
  bool empty() { return pq.empty(); }
  bool size() { return pq.size() - deleted.size(); }
  void push(T e) { pq.push(e); }
  T pop() { return pq.pop(); }
  void remove(T e) {
    if (!pq.empty() && pq.top() == e) {
      pq.pop();
      while (!pq.empty() && !deleted.empty() && pq.top() == deleted.top()) {
        pq.pop();
        deleted.pop();
      }
    } else {
      deleted.push(e);
    }
  }
};

int N;

vector<int> neighbours[200009];
PQ_del<int> child_depths[200009];
int ans[200009];

int dfs(int u, int parent) {
  for (auto v : neighbours[u]) {
    if (v == parent) continue;
    child_depths[u].push(1 + dfs(v, u));
  }

  return child_depths[u].top();
}

void change_root(int u, int v) {
    child_depths[u].remove(1 + child_depths[v].top());
    child_depths[v].push(1 + child_depths[u].top());
}

void walk(int u, int parent) {

  ans[u] = child_depths[u].top();

  for (auto v : neighbours[u]) {
    if (v == parent) continue;
    change_root(u, v);
    walk(v, u);
    change_root(v, u);
  }
}



i32 main() {

  cin >> N;

  for (int i=1; i<=N; i++) {
    child_depths[i].push(0);
  }

  for (int i=0; i<N-1; i++) {
    int a, b;
    cin >> a >> b;
    neighbours[a].push_back(b);
    neighbours[b].push_back(a);
  }

  dfs(1, 1);
  walk(1, 1);

  for (int i=1; i<=N; i++) {
    cout << ans[i] << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS