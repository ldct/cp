#include <bits/stdc++.h>

using namespace std;

// cf: 935ms
class DivisorSieve {
public:
  vector<vector<int32_t>> divisors;
  DivisorSieve(size_t N=1e6+10) {
    divisors = vector<vector<int32_t>>(N, vector<int32_t>());
    for (int32_t i=1; i<N; i++) {
      for (int32_t j=i; j<N; j+=i) {
        divisors[j].push_back(i);
      }
    }
  }
};

int main() {
  auto s = DivisorSieve();
  for (auto d : s.divisors[12]) cout << d << endl;
  return 0;
}
