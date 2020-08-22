#include <bits/stdc++.h>
using namespace std;

int N;
unordered_map<int, int> freqs;

long long score(long long start) {
  if (freqs.count(start) == 0) return 0;
  long long ret = start*freqs[start];

  if (start % 2 != 0) return ret;
  long long next = 3 * (start / 2);

  return ret + score(next);
}

int main() {
  
  cin >> N;

  for (int i=0; i<N; i++) {
    long long a;
    cin >> a;
    if (freqs.count(a) == 0) freqs[a] = 0;
    freqs[a]++;
  }

  long long ret = -1;

  for (const auto& p : freqs) {
    long long a = p.first;
    assert(a > 0);
    ret = max(ret, score(a));
  }

  assert(ret != -1);

  cout << ret << endl;



  return 0;
}
