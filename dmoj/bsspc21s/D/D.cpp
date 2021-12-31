#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

int N, M, K;

bool grid[5009][5009];
vector<pair<pair<int, int>, pair<int,int>>> fills;

bool inc(int a, int b, int c) {
  return a <= b && b <= c;
}

bool check(int n, int m) {
  for (int i=0; i<n; i++) for (int j=0; j<m; j++) {
    bool has_0 = false;
    bool has_1 = false;

    for (int x=i*(N/n); x<(i+1)*(N/n); x++) {
      for (int y=j*(M/m); y<(j+1)*(M/m); y++) {
        if (grid[x][y]) { has_1 = true; } else { has_0 = true; }
      }
    }
    if (has_0 && has_1) return false;
  }
  return true;
}

void ts1() {
  memset(grid, 0, sizeof(grid));
  for (int i=0; i<K; i++) {
    int x, y, X, Y;
    cin >> x >> y >> X >> Y;
    x--; y--; X--; Y--;

    fills.push_back({{x, y}, {X, Y}});
  }

  for (int i=0; i<=N; i++) for (int j=0; j<=M; j++) {
    for (auto [p1, p2] : fills) {
      auto [x, y] = p1; auto [X, Y] = p2;
      if (inc(x, i, X) && inc(y, j, Y)) {
        grid[i][j] = 1; break;
      }
    }
  }

  vector<pair<int, int>> to_check;

  to_check.push_back({N, M});

  while (1) {
    auto [n, m] = to_check[to_check.size()-1];
    if (n % 2 == 0 && m % 2 == 0) {
      to_check.push_back({n / 2, m / 2});
    } else {
      break;
    }
  }

  int ret = 0;
  for (int i=0; i<to_check.size(); i++) {
    auto [n, m] = to_check[i];
    if (check(n, m)) ret = max(ret, i);
  }
  cout << ret << endl;
}

i32 main() {

  cin >> N >> M >> K;

  if (N <= 5000 && M <= 5000) {
    ts1();
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS