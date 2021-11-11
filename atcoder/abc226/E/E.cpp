#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<int> neighbours[200009];
int curr_component = 0;
int component_of[200009];
bool visited[200009];
int_least32_t num_cycles[200009];

int modexp(long long x, unsigned int y, int p) {
    long long res = 1;
    x %= p;

    if (x == 0) return 0;

    while (y > 0) {
        // If y is odd, multiply x with result
        if (y & 1)
            res = (res*x) % p;

        // y must be even now
        y = y>>1; // y = y/2
        x = (x*x) % p;
    }
    return res;
}


void dfs(int u, int daddy) {
  visited[u] = true;
  for (auto v : neighbours[u]) {
    if (v == daddy) continue;
    if (visited[v]) {
      num_cycles[curr_component]++;
      continue;
    };
    dfs(v, u);
  }
}


int main() {

  memset(component_of, -1, sizeof(component_of));
  memset(num_cycles, 0, sizeof(num_cycles));
  memset(visited, 0, sizeof(visited));

  cin >> N >> M;
  for (int i=0; i<M; i++) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    neighbours[u].push_back(v);
    neighbours[v].push_back(u);
  }

  for (int u=0; u<N; u++) {
    if (neighbours[u].size() == 0) {
      cout << 0 << endl;
      return 0;
    }
  }

  for (int u=0; u<N; u++) {
    if (visited[u]) continue;
    dfs(u, -1);
    if (num_cycles[curr_component] != 2) {
      cout << 0 << endl;
      return 0;
    }
    curr_component++;
  }

  cout << modexp(2, curr_component, 998244353) << endl;
  return 0;
}
