#include <bits/stdc++.h>
using namespace std;

long long max_val(long long a, long long b) {
  for (int i=63; i>=0; i--) {
    long long mask = (1LL << i);
    if (!(a&mask) && !(b&mask)) {
      continue;
    }
    if (!(a&mask) && (b&mask)) {
      a ^= mask;
      b ^= mask;
      continue;
    }
    if ((a&mask) && (b&mask)) {
      return a | (mask-1);
    }
    if ((a&mask) && !(b&mask)) {
      continue;
    }
  }
  return a;
}

vector<long long> A;

int main() {

  // cout << max_val(3, 2) << endl;
  // return 0;

  int N;
  cin >> N;
  long long total = 0;
  for (int i=0; i<N; i++) {
    long long a;
    cin >> a;
    A.push_back(a);
    total ^= a;
  }

  long long ret = LLONG_MIN;

  for (const auto a : A) {
    ret = max(ret, max_val(total^a, a));
    // cout << (total ^ a) << " " << a << " " << max_val(total ^ a, a) << endl;
  }
  cout << ret << endl;
}
