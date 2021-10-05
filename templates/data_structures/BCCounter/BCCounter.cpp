#include <bits/stdc++.h>
using namespace std;

template<size_t N=200009>
class BCCounter {
public:
    long long f[N];
    long long ff[N];
    BCCounter() {
        for (int i=0; i<N; i++) f[i] = ff[i] = 0;
        ff[0] = N;
    }
    void inc(int idx) {
        auto v = f[idx];
        ff[v] -= 1;
        f[idx] += 1;
        ff[v+1] += 1;
    }
    void decr(int idx) {
        auto v = f[idx];
        ff[v] -= 1;
        f[idx] -= 1;
        ff[v+1] += 1;
    }
    int num_nonzero() {
        return N - ff[0];
    }
};

int N;

int main() {

  for (int i=0; i<500; i++) {
      auto c = BCCounter<200009>();
  }
      
  return 0;
}
