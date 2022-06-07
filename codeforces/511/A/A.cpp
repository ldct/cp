#include <bits/stdc++.h>

#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t
class Sieve {
public:
  vector<i32> s;
  Sieve(size_t N=1.5e7+100) {
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

  scanf("%lld", &N);

  for (int i=0; i<N; i++) {
    int a;
    scanf("%lld", &a);

    for (auto [p, e] : sieve.fastfactorize_counter(a)) {
      prime_counts[p].push_back(e);
    }
  }

  int ret = INT_MAX;

  for (auto& [p, v] : prime_counts) {
    ret = min(ret, score(p));
  }

  if (ret >= N) ret = -1;
  printf("%lld", ret);

  return 0;
}
