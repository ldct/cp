#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>

using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t
class Sieve {
public:
  vector<int> s;
  Sieve(size_t N=1.5e7+100) {
    s = vector<int>(N, -1);
    s[0] = -1;
    s[1] = -1;
    for (int i=2; i*i < N; i++) {
      if (s[i] != -1) continue;
      for (int j = i; j < N; j += i) {
        if (j > i) s[j] = i;
      }
    }
  }
  vector<pair<int, int>> fastfactorize_counter(int n) {
    vector<pair<int,int>> ret;

    while (s[n] != -1) {
      int p = s[n];
      int e = 0;

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
};

int N;
map<int, vector<int>> prime_counts;

int score(int p) {
  auto& lst = prime_counts[p];
  if (lst.size() < N) return N - lst.size();

  int mv = INT_MAX;

  for (auto x : lst) mv = min(mv, x);

  int ret = 0;

  for (auto e : lst) {
    if (e == mv) ret++;
  }

  return ret;
}

i32 main() {
  auto sieve = Sieve();

  cin >> N;
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;

    auto factors = sieve.fastfactorize_counter(a);

    for (auto [p, e] : factors) {
      prime_counts[p].push_back(e);
    }
  }

  int ret = INT_MAX;

  for (auto& [p, v] : prime_counts) {
    ret = min(ret, score(p));
  }

  if (ret >= N) ret = -1;
  cout << ret << endl;

  return 0;
}
