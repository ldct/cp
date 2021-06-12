#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 10000007;

int d[MAX_N];
int ans[MAX_N];

int main() {

  memset(d, 0, sizeof(d));
  memset(ans, -1, sizeof(ans));

  for (int i=1; i<MAX_N; i++)
    for (int j=i; j<MAX_N; j+=i) d [j] += i;

  for (int i=1; i<MAX_N; i++) {
    auto e = d[i];
    if (e < MAX_N) {
      if (ans[e] == -1) ans[e] = i;
      ans[e] = min(ans[e], i);
    }
  }

  int N; cin >> N;

  for (int i=0; i<N; i++) {
    int x; cin >> x;
    cout << ans[x] << endl;
  }

  return 0;
}
