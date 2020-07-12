#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_K = 10009;

int K;
int A[MAX_K];
int memo[MAX_K][4];

int match(int a, int aa, int b, int bb) {
  if (a == aa && b == bb) return 0;
  if (a < aa && b < bb) return 0;
  if (a > aa && b > bb) return 0;
  return 1;
}

int dp(int start, int note) {
  // smallest rule-breaks for writing the interval [start, K] where we use `note` at start 
  if (start >= K-1) return 0;

  assert(start+1 < K);

  if (memo[start][note] != -1) {
    // cout << "cache hit " << start << " " << note << " " << memo[start][note] << endl; 
    return memo[start][note];
  } else {
    // cout << "cache miss " << start << " " << note << endl; 
  }

  int a = A[start];
  int next_a = A[start+1];

  int ret = INT_MAX;
  for (int next_note=0; next_note<4; next_note++) {
    ret = min(ret, 
      match(a, next_a, note, next_note) + dp(start+1, next_note)
    );
  }
  return memo[start][note] = ret;
}

int ans() {
  if (K <= 3) return 0;
  auto ret = INT_MAX;
  for (int note=0; note<4; note++) {
    ret = min(ret, dp(0, note));
  }
  return ret;
}

int main() {

  int T;

  cin >> T;

  for (int i=1; i<=T; i++) {
    cin >> K;

    for (int j=0; j<K; j++) {
      for (int n=0; n<4; n++) {
        memo[j][n] = -1;
      }
    }

    for (int k=0; k<K; k++) {
      cin >> A[k];
    }
    cout << "Case #" << i << ": " << ans() << endl;
  }  
  
  return 0;
}
