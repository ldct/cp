#include <bits/stdc++.h>
using namespace std;

int N;

constexpr size_t MAX_A = 5000009;

long long cnt[MAX_A];
long long best_inc[MAX_A];

int main() {

  cin >> N;
  for (long long i=0; i<N; i++) {
    long long a;
    cin >> a;
    assert(a < MAX_A);
    cnt[a]++;
  }

  for (long long i=0; i<MAX_A; i++) {
    best_inc[i] = cnt[i]*(i-1);
  }

  for (long long i=2; i<MAX_A; i++) {
    for (long long j=2*i; j<MAX_A; j+=i) {
      // cout << i << "->" << j << endl;
      // update i->j
      best_inc[j] = max(best_inc[j], cnt[j]*(j-1) + best_inc[i]);
    }
  }

  long long ret = 0;
  for (long long i=2; i<MAX_A; i++) {
    ret = max(ret, best_inc[i]);
  }
  ret += N;
  cout << ret << endl;

  return 0;
}
