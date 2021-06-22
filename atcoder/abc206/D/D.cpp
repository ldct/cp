#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int N;
int A[200009];
set<int> leaders;

int main() {

  cin >> N;

  for (int i=0; i<N; i++) {
    cin >> A[i];
  }

  dsu d(200009);

  for (int i=0; i<N; i++) {
    d.merge(A[i], A[N-1-i]);
  }

  for (int i=0; i<N; i++) {
    leaders.insert(d.leader(A[i]));
  }

  int ret = 0;

  for (const auto l : leaders) {
    ret += (d.size(l) - 1);
  }

  cout << ret << endl;

  return 0;
}
