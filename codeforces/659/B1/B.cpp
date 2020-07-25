#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 109;
constexpr size_t MAX_K = 109;
constexpr int MAX_TTS = 4*MAX_K*MAX_K;

int D[MAX_N];
int P[2*MAX_K];

char memo[MAX_N][MAX_TTS];

int N, K, L;

bool ok(int pos, int time) {
  // whether she can make it if she is at `pos` at `time`
  if (pos > N+1) return false;
  if (pos < 0) return false;
  if (time > MAX_TTS) return false;
  if (pos == N+1) return true;

  if (memo[pos][time] != -1) return memo[pos][time];

  if (0 < pos && pos <= N) {
    if (D[pos-1] + P[time % (2*K)] > L) return memo[pos][time] = false;
  }
  return memo[pos][time] = (ok(pos, time+1) || ok(pos+1, time+1));
}

int main() {

  int T;
  cin >> T;

  while (T --> 0) {

    for (int i=0; i<MAX_N; i++) for (int j=0; j<MAX_TTS; j++) memo[i][j] = -1;

    cin >> N >> K >> L;
    for (int i=0; i<N; i++) {
      cin >> D[i];
    }
    // cout << "P= ";
    for (int i=0;i<2*K;i++) {
      if (i <= K) {
        P[i] = i;
      } else {
        P[i] = 2*K-i;
      }
      // cout << P[i] << " ";
    }
    // cout << endl;

    if (ok(0, 0)) {
      cout << "Yes" << endl;
    } else {
      cout << "No" << endl;
    }
  }  

    
  return 0;
}
