#include <bits/stdc++.h>

using namespace std;

class DivisorSieve {
public:
  vector<vector<int>> divisors;
  DivisorSieve(size_t N=5e5) {
    divisors = vector<vector<int>>(N, vector<int>());
    for (int i=1; i<N; i++) {
      for (int j=i; j<N; j+=i) {
        if (i == j) continue;
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
