#include <bits/stdc++.h>
using namespace std;

constexpr int MODULUS = 1000000007;

int N, K, Q;

long long factor[5009][5009];
long long A[5009];

int main() {

  memset(factor, 0, sizeof(factor));

  cin >> N >> K >> Q;

  for (int i=0; i<N; i++) {
    cin >> A[i];
  }

  // DP to populate factor

  K++;
  for (int i=0; i<N; i++) {
    factor[0][i] = 1;
  }
  for (int k=1; k<K; k++) {
    for (int i=0; i<N; i++) {
      if (i-1 >= 0) factor[k][i] += factor[k-1][i-1];
      if (i+1 < N) factor[k][i] += factor[k-1][i+1];
      factor[k][i] %= MODULUS;
    }
  }

  K--;

  for (int i=0; i<N; i++) {
    cout << factor[K][i] << " ";
  }
  cout << endl;

  long long initial = 0;
  for (int i=0; i<N; i++) {
    initial += factor[K][i] * A[i];
  }

  for (int q=0; q<Q; q++) {
    int idx, na;
    cin >> idx >> na;
    idx--;

    initial += (factor[K][idx] * (na - A[idx]));
    initial %= MODULUS;
    initial += MODULUS;
    initial %= MODULUS;

    cout << (2*initial) % MODULUS << endl;
    A[idx] = na;
  }

  return 0;
}
