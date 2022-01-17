#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

int N, L, K;
int D[509];
int A[509];

int ans(int i, int j, int k) {

  int ret = (D[i+1] - D[i])*A[i] + ans(i+1, i, k);
  if (k > 0) ret = min(ret, (D[i+1] - D[i])*A[j] + ans(i+1, j, k-1));

  return ret;
}


i32 main() {


  cin >> N >> L >> K;

  for (int i=0; i<N; i++) cin >> D[i];
  for (int i=0; i<N; i++) cin >> A[i];
  D[N] = L;

  int ret = D[1]*A[0];

  int i=N;
  int memo1[509][509];
  int memo2[509][509];

  memset(memo1, 0, sizeof(memo1));

  int (*memo)[509][509] = &memo1;
  int (*old_memo)[509][509] = &memo2;

  while (1) {
    if (i == 1) break;

    i -= 1;

    swap(memo, old_memo);

    for (int j=0; j<N; j++) for (int k=0; k<N; k++) {
      (*memo)[j][k] = (D[i+1] - D[i])*A[i] + (*old_memo)[i][k];
      if (k > 0) (*memo)[j][k] = min((*memo)[j][k], (D[i+1] - D[i])*A[j] + (*old_memo)[j][k-1]);
    }

    if (i == 1) break;
  }

  ret += (*memo)[0][K];

  cout << ret << endl;

  return 0;
}
