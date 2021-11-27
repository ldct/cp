#include <bits/stdc++.h>
using namespace std;

int N;

constexpr size_t MAX_A = 200009;

long long cnt[MAX_A];
long long best[MAX_A];

int main() {

  int T;
  cin >> T;
  while (T --> 0) {
    memset(cnt, 0, sizeof(cnt));
    memset(best, 0, sizeof(best));
    cin >> N;
    for (long long i=0; i<N; i++) {
      long long a;
      cin >> a;
      cnt[a]++;
    }
    for (int i=0; i<N; i++) {
      best[i] = cnt[i];
    }
    for (long long i=1; i<MAX_A; i++) {
      for (long long j=2*i; j<MAX_A; j+=i) {
        best[j] = max(best[j], cnt[j]+best[i]);
        // if (best[j] == 3) {
        //   cout << i << "->" << j << endl;
        // }
      }
    }
    long long ret = 0;
    for (int i=0; i<MAX_A; i++) ret = max(ret, best[i]);
    cout << (N-ret) << endl;
  }

  return 0;
}
