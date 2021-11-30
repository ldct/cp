#include <bits/stdc++.h>
using namespace std;

int N;

constexpr size_t MAX_A = 500009;

vector<int> num_dividing(vector<int>& A) {
  vector<int> ret(MAX_A, 0);
  vector<int> cnt(MAX_A, 0);
  for (auto a : A) {
    assert(a > 0);
    cnt[a]++;
  }

  for (int i=2; i<MAX_A; i++) {
    for (int j=i; j<MAX_A; j+=i) {
      ret[i] += cnt[j];
    }
  }

  ret[1] = A.size();
  return ret;
}

class DivisorSieve {
public:
  vector<vector<int>> divisors;
  DivisorSieve(size_t N=MAX_A) {
    divisors = vector<vector<int>>(N, vector<int>());
    for (int i=1; i<N; i++) {
      for (int j=i; j<N; j+=i) {
        if (i == j) continue;
        divisors[j].push_back(i);
      }
    }
  }
};

vector<int> nd;
DivisorSieve ds;

int memo[MAX_A];

int ans(int i) {
  if (i == 1) return 0;
  if (memo[i] != -1) return memo[i];
  int ret = 0;
  for (auto d : ds.divisors[i]) {
    assert(nd[d] >= nd[i]);
    ret = max(ret, ans(d) + d*(nd[d] - nd[i]));
  }
  return memo[i] = ret;
}

int main() {
  memset(memo, -1, sizeof(memo));
  int N;
  vector<int> arr;
  cin >> N;
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    arr.push_back(a);
  }

  nd = num_dividing(arr);


  int ret = -1;

  for (auto a : arr) {
    // cout << a << " " << ans(a) << " " << (a*nd[a]) << endl;
    ret = max(ret, ans(a) + a*nd[a]);
  }
  cout << ret << endl;

  return 0;
}
