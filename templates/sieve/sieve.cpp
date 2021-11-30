#include <bits/stdc++.h>

using namespace std;

class Sieve {
public:
  vector<int> s;
  Sieve(size_t N=1e7) {
    s = vector<int>(N, -1);
    s[0] = 0;
    s[1] = 0;
    for (int i=2; i*i < N; i++) {
      if (s[i] != -1) continue;
      for (int j = i; j < N; j += i) {
        if (j > i) s[j] = i;
      }
    }
  }
  int count_primes() {
    int ret=0;
    for (auto f : s) if (f == -1) ret += 1;
    return ret;
  }
};

int main() {
  auto s = Sieve();
  cout << "there are " << s.count_primes() << " primes less than 10^7" << endl;
  return 0;
}
