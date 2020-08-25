#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 300009;

int N;
vector<int> neighbours[MAX_N];
int max_depth;
int depth_of[MAX_N];

void dfs(int u, int parent, int depth) {
  depth_of[u] = depth;
  max_depth = max(max_depth, depth);
  for (const auto& v : neighbours[u]) {
    if (v == parent) continue;
    dfs(v, u, depth+1);
  }
}

int main() {
  
  cin >> N;
  for (int i=0; i<N-1; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    neighbours[a].push_back(b);
    neighbours[b].push_back(a);
  }

  max_depth = -1;
  dfs(0, 0, 0);

  int new_root;
  for (int i=0; i<N; i++) {
    if (depth_of[i] == max_depth) {
      new_root = i;
    }
  }

  max_depth = -1;
  dfs(new_root, new_root, 0);


  cout << 3*max_depth << endl;
    
  return 0;
}
