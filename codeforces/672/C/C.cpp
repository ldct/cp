#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 300009;

int N, Q;
long long A[MAX_N];
long long memo[MAX_N][2];

long long ans(int start, int next_factor) {
  if (start == N) return 0;

  int mk = (next_factor + 1) / 2;

  if (memo[start][mk] != -1) return memo[start][mk];

  assert(next_factor == -1 || next_factor == 1);

  return memo[start][mk] = max(
    next_factor*A[start] + ans(start+1, -1*next_factor),
    ans(start+1, next_factor)
  );

}

int main() {

  int T;
  cin >> T;

  while (T --> 0) {
    cin >> N >> Q;
    assert(Q == 0);
    
    for (int i=0; i<N; i++) {
      memo[i][0] = memo[i][1] = -1; 
      cin >> A[i];
    }

    cout << ans(0, 1) << endl;

  }
      
  return 0;
}
