#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int N, M;
char grid[109][109];
int colour[109][109];
int next_colour = 0;

int sz[10009];
int max_x[10009];
int max_y[10009];
int min_x[10009];
int min_y[10009];

void dfs(int i, int j) {
  if (!(0 <= i)) return;
  if (!(i < N)) return;
  if (!(0 <= j)) return;
  if (!(j < M)) return;

  if (colour[i][j] != -1) return;
  if (grid[i][j] != '1') return;
  colour[i][j] = next_colour;

  sz[next_colour]++;
  min_x[next_colour] = min(min_x[next_colour], i);
  min_y[next_colour] = min(min_y[next_colour], j);
  max_x[next_colour] = max(max_x[next_colour], i);
  max_y[next_colour] = max(max_y[next_colour], j);

  dfs(i+1, j);
  dfs(i-1, j);
  dfs(i, j+1);
  dfs(i, j-1);
}

int sq(int s) {
  return (max_x[s] - min_x[s] + 1) * (max_y[s] - min_y[s] + 1);
}

void ans() {
  for (int i=0; i<next_colour; i++) {
    if (sz[i] != sq(i)) {
      cout << "NO" << endl;
      // cout << i << endl;
      // cout << min_y[i] << endl;
      // cout << max_y[i] << endl;

      return;
    }
  }
  cout << "YES" << endl;
}

i32 main() {

  int T;
  cin >> T;

  while (T --> 0) {
    next_colour = 0;
    memset(colour, -1, sizeof(colour));
    memset(sz, 0, sizeof(sz));

    for (int i=0; i<10009; i++) {
      min_x[i] = INT_MAX;
      min_y[i] = INT_MAX;
      max_x[i] = -1;
      max_y[i] = -1;
    }

    cin >> N >> M;
    for (int i=0; i<N; i++) {
      for (int j=0; j<M; j++) {
        cin >> grid[i][j];
      }
    }

    for (int i=0; i<N; i++) {
      for (int j=0; j<M; j++) {
        if (colour[i][j] != -1) continue;
        if (grid[i][j] != '1') continue;
        dfs(i, j);
        next_colour++;
      }
    }

    ans();

    // for (int i=0; i<N; i++) {
    //   for (int j=0; j<M; j++) {
    //     if (grid[i][j] == '1') {
    //       cout << colour[i][j];
    //     } else {
    //       cout << " ";
    //     }
    //   }
    //   cout << endl;
    // }
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS