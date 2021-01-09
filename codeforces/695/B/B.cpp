#include <bits/stdc++.h>
using namespace std;

int T, N;

bool is_hv(vector<int>& A, int i) {
  if (!(0 <= i-1)) return false;
  if (!(i+1 < A.size())) return false;
  if (A[i] > max(A[i-1], A[i+1])) return true;
  if (A[i] < min(A[i-1], A[i+1])) return true;
  return false;
}

int count_hv(vector<int>& A) {
  int ret = 0;
  for (int i=0; i<A.size(); i++) {
    if (is_hv(A, i)) ret += 1;
  }
  return ret;
}

int decrease_three(vector<int>& A) {
  for (int i=0; i<A.size(); i++) {
    if (is_hv(A, i) && is_hv(A, i+1) && is_hv(A, i+2)) return true;
  }
  return false;
}

int ans(vector<int>& A) {
  int initial_hv = count_hv(A);

  if (initial_hv == 0 || initial_hv == 1) return 0;
  if (decrease_three(A)) return initial_hv - 3;
  if (decrease_two(A)) return initial_hv - 2;

  return initial_hv-1;
}

int main() {

  cin >> T;
  while (T--) {
    cin >> N;
    int a;
    vector<int> A;
    for (int i=0; i<N; i++) {
      cin >> a;
      A.push_back(a);
    }
    cout << ans(A) << endl;
  }
  return 0;
}
