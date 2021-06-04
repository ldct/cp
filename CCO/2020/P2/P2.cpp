#include <bits/stdc++.h>

using namespace std;

int N;
vector<int> A;
vector<int> B;
int T, U;

int rightmost() {
  for (int j=T; j!=-1; j--) {
    cout << "in rightmost loop" << j << endl;
    if (B[j] < A[j]) {
      return T = j;
    }
  }
  return -1;
}

int leftmost(int i, int cap) {
  cout << "leftmost " << i << " " << cap << endl;
  U = min(U, i);
  for (int k=U; k!=-1; k--) {
    cout << "in leftmost loop" << k << endl;
    if (A[k] <= cap) return k;
  }
  return -1;
}

int main() {

  cin >> N;
  for (int i=0; i<N; i++) {
    int b;
    cin >> b;
    B.push_back(b);
    A.push_back(i+1);
  }

  T = N-1;
  U = N;

  long long ret = 0;

  while (1) {
    int j = rightmost();
    if (j == -1) {
      cout << ret << endl; return 0;
    }

    int i = leftmost(j, B[j]);
    if (i == -1) {
      cout << -1 << endl; return 0;
    }

    A.erase(A.begin() + i);
    ret += (long long)(j-i);
    T -= 1;
  }

  return 0;
}
