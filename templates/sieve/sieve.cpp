#include <bits/stdc++.h>

using namespace std;
#define i32 int32_t

class Sieve {
public:
  vector<i32> s;
  Sieve(size_t N=1e7) {
    s = vector<i32>(N, -1);
    s[0] = -1;
    s[1] = -1;
    for (int i=2; i*i < N; i++) {
      if (s[i] != -1) continue;
      for (int j = i; j < N; j += i) {
        if (j > i) s[j] = i;
      }
    }
  }
  vector<pair<i32, i32>> fastfactorize_counter(i32 n) {
    vector<pair<i32,i32>> ret;

    while (s[n] != -1) {
      i32 p = s[n];
      i32 e = 0;

      while (n % p == 0) {
        e++;
        n /= p;
      }

      ret.push_back({p, e});
    }

    if (n > 1) {
      ret.push_back({n, 1});
    }
    return ret;

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
