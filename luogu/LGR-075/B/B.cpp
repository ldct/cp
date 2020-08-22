#include <bits/stdc++.h>
using namespace std;

int N, K;
unordered_map<long long, long long> freqs;

int main() {
  
  cin >> N >> K;
  for (int i=0; i<N; i++) {
    long long a, b;
    cin >> a >> b;
    if (freqs.count(a) == 0) freqs[a] = 0;
    freqs[a] += b;
  }

  if (K == 0) {
    long long ret = -1;
    for (const auto& p : freqs) {
      long long a = p.first;
      long long b = p.second;
      if (b > 1) {
        ret = max(ret, a*b);
      }
    }
    if (ret == -1) {
      cout << "NO" << endl;
      return 0;
    }
    cout << ret << endl;
    return 0;
  }

  long long ret = -1;

  for (const auto& p : freqs) {
    long long a = p.first;
    long long b = p.second;

    if (freqs.count(K+a) == 0) continue;

    long long f = min(freqs[a], freqs[K+a]);
    ret = max(ret, f*(a+K+a));
  }

    if (ret == -1) {
      cout << "NO" << endl;
      return 0;
    }
    cout << ret << endl;
    return 0;
}
