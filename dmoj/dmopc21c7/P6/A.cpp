#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int N, M, MODULUS, X_MIN;

bool is_vertex(int x, int y) {
  int r2 = x*x + y*y;
  return (N*N <= r2) && (r2 < (N+M)*(N+M));
}

bool subset(int m1, int m2) {
  return (m1 | m2) == m2;
}

bool is_bit_set(int mask, int i) {
  return mask & (1 << i);
}

int y_mask(int y) {
  int ret = 0;

  int i=0;
  for (int x=X_MIN; x< N+M; x++) {
    if (is_vertex(x, y)) {
      ret |= (1 << i);
    } else {
    }
    i += 1;
  }
  return ret;
}

int x_mask(int x) {
  int ret = 0;

  for (int y=0; y<N+M; y++) {
    if (is_vertex(x, y)) {
      ret |= (1 << y);
    } else {
    }
  }
  return ret;
}

int memo[40][1 << 15];

int _unused_ans(int x, int mask) {
  // number of subgraphs of the graph [X_MIN ... x] whene the last row mas `mask` selected
  // no edges allowed

  auto xm = x_mask(x);

  if (memo[x+N+M-1][mask] != -1) return memo[x+N+M-1][mask];

  if (x == X_MIN) {
    if (subset(mask, xm)) return 1;
    return 0;
  }

  xm = x_mask(x-1);

  int ret = 0;

  for (int mask2=xm;;mask2=(mask2-1)&xm) {
    assert(subset(mask2, xm));
    ret += _unused_ans(x-1, mask2);
    ret %= MODULUS;
    if (mask2 == 0) break;
  }

  return memo[x+N+M-1][mask] = ret;
}

int count_adjacent(int m) {
  int r = 0;
  for (int i=0; i<20; i++) {
    if (is_bit_set(m, i) && is_bit_set(m, i+1)) {
      r++;
    }
  }
  return r;
}

int ans(int x, i32 mask) {
  // number of subgraphs of the graph [1-(N+M) ... x] whene the last row mas `mask` selected

  auto xm = x_mask(x);

  if (memo[x+N+M-1][mask] != -1) return memo[x+N+M-1][mask];

  if (x == X_MIN) {
    if (subset(mask, xm)) return (1 << count_adjacent(mask)) % MODULUS;
    return 0;
  }

  xm = x_mask(x-1);

  int ret = 0;

  for (i32 mask2=xm;;mask2=(mask2-1)&xm) {
    assert(subset(mask2, xm));
    int r = ans(x-1, mask2);
    r *= (1 << bitset<32>(mask2 & mask).count()) % MODULUS;
    ret += r;
    ret %= MODULUS;
    if (mask2 == 0) break;
  }

  if (x == X_MIN) {
    cout << "ret=" << ret << "adj=" << count_adjacent(mask) << endl;
  }

  ret *= (1 << count_adjacent(mask));
  ret %= MODULUS;

  return memo[x+N+M-1][mask] = ret;
}

i32 main() {

  memset(memo, -1, sizeof(memo));

  cin >> N >> M >> MODULUS;
  X_MIN = 1-(N+M);

  // count total number of vertices
  // int r = 0;
  // for (int x=1-(N+M); x< N+M; x++) {
  //   for (int y=0; y<N+M; y++) {
  //     if (is_vertex(x, y)) r++;
  //   }
  // }
  // cout << r << endl;

  cout << ans(N+M, 0) << endl;

  return 0;
}
