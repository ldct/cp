#pragma GCC target ("avx2")
#pragma GCC optimization ("O3")
#pragma GCC optimization ("unroll-loops")

#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

int N, K, flipped;
vector<int> A, B;
i32 dp[1609][1609];
int SUM_A, SUM_B;

i32 main() {

  int T;
  cin >> T;
  while (T --> 0) {
    SUM_A = 0;
    SUM_B = 0;
    A.clear();
    B.clear();
    cin >> N >> K;
    for (int i=0; i<N; i++) {
      int a; cin >> a; A.push_back(a);
      SUM_A += a;
    }
    for (int i=0; i<N; i++) {
      int b; cin >> b; B.push_back(b);
      SUM_B += b;
    }

    if (K == N) {
      cout << min(SUM_A, SUM_B) << endl;
      continue;
    }

    if (K > N/2) {
      K = N-K;
      flipped = true;
    } else {
      flipped = false;
    }

    memset(dp, 0, sizeof(dp));

    for (i32 i=0; i<N; i++) {
      for (i32 a=SUM_A+1; a>=0 ;a--) for (i32 b=SUM_B+1; b>=0 ;b--) {
        if (dp[a][b] == 0) continue;
        i32 aa = a + A[i];
        i32 bb = b + B[i];

        dp[aa][bb] |= (dp[a][b] << 1);
        dp[aa][bb] &= ((1 << 30) - 1);
      }
      dp[A[i]][B[i]] |= 1;
    }

    int ret = -1;
    for (int a=0; a<1600 ;a++) for (int b=0; b<1600; b++) {
      if (dp[a][b] & (1L << (K-1))) {
        if (flipped) {
          ret = max(ret, min(SUM_A - a, SUM_B - b));
        } else {
          ret = max(ret, min(a, b));
        }
      }
    }

    cout << ret << endl;
  }

  return 0;
}
