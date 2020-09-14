#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 200009;

int N;
int boss[MAX_N];
long long memo[MAX_N];

long long ans(int x) {
  if (x >= N) return 0;

  if (memo[x] != -1) return memo[x];

  long long ret = LLONG_MAX;

  ret = min(ret, boss[x] + ans(x+2));
  ret = min(ret, boss[x] + ans(x+3));

  if (x+1 < N) ret = min(ret, boss[x] + boss[x+1] + ans(x+4));
  if (x+1 < N) ret = min(ret, boss[x] + boss[x+1] + ans(x+3));

  return memo[x] = ret;
}

int main() {
  
  int T;
  cin >> T;

  while (T --> 0) {
    cin >> N;

    for (int i=0; i<N; i++) memo[i] = -1;

    for (int i=0; i<N; i++) {
      cin >> boss[i];
    }

    cout << ans(0) << endl;

  }
    
  return 0;
}
