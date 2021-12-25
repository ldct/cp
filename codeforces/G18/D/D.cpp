#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

bool invalid;
int T, N, M;
vector<pair<int, int>> neighbours[200009];
int constraints[200009];

i32 main() {

  cin >> T;
  while (T --> 0) {
    cin >> N >> M;
    invalid = false;
    for (int i=0; i<N; i++) { neighbours[i].clear(); constraints[i] = -1; }
    for (int i=0; i<N-1; i++) {
      int x, y, v;
      cin >> x >> y >> v;
      x--; y--;
      neighbours[x].push_back({y, v}); neighbours[y].push_back({x, v});
    }
    for (int i=0; i<M; i++) {
      int a, b, p;
      cin >> a >> b >> p;
      a--; b--;
      if (constraints[a] != -1) { invalid = true; }
      constraints[a] = p;
      if (constraints[b] != -1) { invalid = true; }
      constraints[b] = p;
    }
    if (invalid) {
      cout << "NO" << endl;
      continue;
    }
  }

  cout << "YES?" << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS