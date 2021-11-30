#include <bits/stdc++.h>
using namespace std;

int N;

constexpr size_t MAX_A = 5000009;

vector<long long> num_dividing(vector<long long>& A) {
  vector<long long> ret(MAX_A, 0);
  vector<long long> cnt(MAX_A, 0);
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


vector<long long> nd;

long long ans[MAX_A];

int main() {
  memset(ans, 0, sizeof(ans));
  int N;
  vector<long long> arr;
  cin >> N;
  for (int i=0; i<N; i++) {
    long long a;
    cin >> a;
    arr.push_back(a);
  }

  nd = num_dividing(arr);

  for (long long i=1; i<MAX_A; i++) {
    for (long long j=i; j<MAX_A; j+=i) {
      if (i == j) continue;
      // i -> j
      ans[j] = max(ans[j], ans[i] + i*(nd[i] - nd[j]));
    }
  }

  long long ret = -1;

  for (long long a : arr) {
    ret = max(ret, ans[a] + a*nd[a]);
  }
  cout << ret << endl;

  return 0;
}
