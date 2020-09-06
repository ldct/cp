#include <bits/stdc++.h>
using namespace std;

int N, K;
vector<int> A;

int max_vec(vector<int>& A) {
  int ret = INT_MIN;
  for (const auto a : A) {
    ret = max(ret, a);
  }
  return ret;
}

bool all_le(vector<int>& A, int K) {
  for (const auto a : A) {
    if (a > K) return false;
  }
  return true;
}

int count(vector<int>& A, int x, int K) {
  int ret = 0;
  for (const auto a : A) {
    if ((a^x) <= K) ret++;
  }
  return ret;
}

int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  
  cin >> N >> K;
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A.push_back(a);
  }

  if (all_le(A, K)) {
    cout << N << endl;
    return 0;
  }

  int M = 1024;
  int ret = -1;
  for (int x = 0; x <= M; x++) {
    ret = max(ret, count(A, x, K));
  }

  cout << ret << endl;

  return 0;

}
