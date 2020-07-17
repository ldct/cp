#include <bits/stdc++.h>
using namespace std;

constexpr int MODULUS = 1000000007;

class SquareArray {
public:
  vector<long long> storage;
  vector<long long> tmp;
  int N;

 SquareArray(int N) {
   this->N = N;
   this->storage = vector<long long>(N*N, 0);
   this->tmp = vector<long long>(N*N, 0);
 }

 void rmul(const SquareArray* B) {
   for (int i=0; i<N*N; i++) tmp[i] = 0;
   for (int i=0; i<N; i++) for (int j=0; j<N; j++) for (int k=0; k<N; k++) {
     tmp[i*N + k] += (storage[i*N+j]*B->storage[j*N+k]) % MODULUS;
     tmp[i*N + k] %= MODULUS;
   }
   swap(tmp, storage);
 }

  void lmul(const SquareArray* B) {
   for (int i=0; i<N*N; i++) tmp[i] = 0;
   for (int i=0; i<N; i++) for (int j=0; j<N; j++) for (int k=0; k<N; k++) {
     tmp[i*N + k] += (B->storage[i*N+j]*storage[j*N+k]) % MODULUS;
     tmp[i*N + k] %= MODULUS;
   }
   swap(tmp, storage);
 }

 static SquareArray identity(int n) {
   SquareArray ret = SquareArray(n);
   for (int i=0; i<n; i++) ret.storage[i*n+i] = 1;
   return ret;
 }

 void pow(int exponent) {
   SquareArray result = identity(N);
   while (exponent > 0) {
     if (exponent % 2 == 1) result.lmul(this);
     this->rmul(this);
     exponent /= 2;
   }
   this->storage = result.storage;
 }

};

int main() { 
  int N, M, K;
  cin >> N >> M >> K;
  SquareArray adjacency = SquareArray(N);

  for (int i=0; i<M; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    adjacency.storage[a*N+b] = 1;
  }

  adjacency.pow(K);

  int ret = 0;

  for (int i=0; i<N; i++) for (int j=0; j<N; j++) {
    ret += adjacency.storage[i*N+j];
    ret %= MODULUS;
  }

  cout << ret << endl;

  return 0;
}
