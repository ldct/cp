#include <bits/stdc++.h>
using namespace std;

constexpr long long MODULUS = 4294967296;

class SquareArray {
public:
  vector<unsigned long long> storage;
  vector<unsigned long long> tmp;
  int N;

 SquareArray(int N) {
   this->N = N;
   this->storage = vector<unsigned long long>(N*N, 0);
   this->tmp = vector<unsigned long long>(N*N, 0);
 }

  void set(int x, int y, long long val) {
   this->storage[x*N + y] = val;
  }

  unsigned long long get(int x, int y) {
   return this->storage[x*N + y];
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

 void pow(long long exponent) {
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
  long long k;
  cin >> k;

  SquareArray adjacency = SquareArray(65);

  for (int i=0; i<8; i++) for (int j=0; j<8; j++) {
    int x = i*8 + j;
    adjacency.set(x, 64, 1);
    for (int k=0; k<8; k++) for (int l=0; l<8; l++) {
      int y = k*8 + l;
      auto c = make_pair(abs(i-k), abs(j-l));
      if (c == make_pair(1, 2) || c == make_pair(2, 1)) {
        adjacency.set(x, y, 1);
      }
    }
  }
  adjacency.set(64, 64, 1);

  adjacency.pow(k+1);

  cout << adjacency.get(0, 64) << endl;

  // for (int i=0; i<65; i++) {
  //   for (int j=0; j<65; j++) {
  //     cout << adjacency.get(i, j) << " ";
  //   }
  //   cout << endl;
  // }

}
