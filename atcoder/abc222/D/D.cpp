#include <bits/stdc++.h>
using namespace std;

int N;
long long A[3009];
long long B[3009];
long long memo_ans[3009][3009];

constexpr long long MODULUS = 998244353;

long long ans(int i, long long lb);

long long ans_sum(int i, int a) {
  long long ret = 0;
  for (long long x = 0; x <= a; x++) {
    ret += ans(i+1, x);
    ret %= MODULUS;
  }
  return ret;
}

long long ans_sum2(int i, int a, int b) {
  cout << "i=" << i << endl;
  if (i >= N) return 0;
  if (!(a <= b)) return 0;
  if (a == 0) return ans_sum(i, b);
  return ans_sum(i, b) - ans_sum(i, a-1);
}

long long ans(int i, long long lb) {
  lb = max(lb, A[i]);
  if (i == N-1) {
    if (!(lb <= B[i])) return 0;
    return B[i] - lb + 1;
  }
  if (!(lb <= B[i])) return 0;

  if (memo_ans[i][lb] != -1) return memo_ans[i][lb];

  long long ret = 0;
  for (long long x = lb; x <= B[i]; x++) {
    ret += ans(i+1, x);
    ret %= MODULUS;
  }
  return memo_ans[i][lb] = ret;
}
int main() {

  memset(memo_ans, -1, sizeof(memo_ans));

  cin >> N;
  for (int i=0; i<N; i++) cin >> A[i];
  for (int i=0; i<N; i++) cin >> B[i];

  cout << ans(0, -1) << endl;

  return 0;
}
