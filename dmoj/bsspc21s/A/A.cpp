#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

struct UF_grid {
  vector<int> e;
  int r; int c;
  UF_grid(int _r, int _c, int n) {
    r = _r; c = _c;
    e = vector<int>(r*c+n, -1);
  }
  int conv(int x, int y) {
    if (x < 0) return r*c - 1 - x;
    return x*c + y;
  }
  bool sameSet(int a, int b) { return find(a) == find(b); }
  int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
  bool join(int a, int b) {
    a = find(a), b = find(b);
    if (a == b) return false;
    if (e[a] > e[b]) swap(a, b);
    e[a] += e[b]; e[b] = a;
    return true;
  }

  bool sameSet(int a, int b, int c, int d) { return sameSet(conv(a, b), conv(c, d)); }
  int find(int a, int b) { return find(conv(a, b)); }
  bool join(int a, int b, int c, int d) { return join(conv(a, b), conv(c, d)); }
};

int N, M;
char grid[2009][2009];
int candidates_of[4000009];

char select(int s) {
  for (char c = 'a'; c <= 'z'; c++) {
    if (s & (1 << (c - 'a'))) return c;
  }
  assert(false);
  return 'z';
}

i32 main() {

  memset(candidates_of, 0, sizeof(candidates_of));

  cin >> N >> M;
  for (int i=0; i<N; i++) for (int j=0; j<M; j++) {
    cin >> grid[i][j];
  }

  auto uf = UF_grid(N, M, 0);

  for (int x=0; x<N; x++) for (int y=0; y<M; y++) {
    uf.join(x, y, x, M-y-1);
    uf.join(x, y, N-x-1, y);
  }

  for (int x=0; x<N; x++) for (int y=0; y<M; y++) {
    auto p = uf.find(x, y);
    if (grid[x][y] != '.') candidates_of[p] |= (1 << (grid[x][y] - 'a'));
  }

  bool ok = true;

  for (int i=0; i<N*M; i++) {
    if (candidates_of[i] == 0) candidates_of[i] = 16;
    if (__builtin_popcount(candidates_of[i]) > 1) ok = false;
  }

  if (!ok) {
    cout << (-1) << endl;
    return 0;
  }

  for (int x=0; x<N; x++) for (int y=0; y<M; y++) {
    auto p = uf.find(x, y);
    grid[x][y] = select(candidates_of[p]);
  }

  for (int x=0; x<N; x++) {
    for (int y=0; y<M; y++) {
      cout << grid[x][y];
    }
    cout << endl;
  }


  return 0;
}
