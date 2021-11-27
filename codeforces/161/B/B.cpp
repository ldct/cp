// https://codeforces.com/problemset/problem/264/B

#include <bits/stdc++.h>
using namespace std;

int N;

constexpr size_t MAX_A = 200009;

long long cnt[MAX_A];
long long best[MAX_A];

int main() {

  cin >> N;
  for (long long i=0; i<N; i++) {
    long long a;
    cin >> a;
    cnt[a] = 1;
  }
  for (int i=0; i<N; i++) {
    best[i] = cnt[i];
  }
  for (long long i=1; i<MAX_A; i++) {
    for (long long j=2*i; j<MAX_A; j+=i) {
      best[j] = max(best[j], cnt[j]+best[i]);
    }
  }
  long long ret = 0;
  for (int i=0; i<MAX_A; i++) ret = max(ret, best[i]);
  cout << ret << endl;
}
