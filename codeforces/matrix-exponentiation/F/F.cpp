#include <bits/stdc++.h>
using namespace std;

class SquareArray {
public:
  vector<long long> storage;
  vector<long long> tmp;
  int N;

  SquareArray(int N) {
    this->N = N;
    this->storage = vector<long long>(N*N, LLONG_MAX);
    this->tmp = vector<long long>(N*N, LLONG_MAX);
  }

  friend ostream& operator << (ostream& os, const SquareArray& s) {

    for (int i=0; i<s.N; i++) {
      for (int j=0; j<s.N; j++) {
        os << s.get(i, j) << "\t";
      }
      os << endl;
    }
    return os;
  }

  void set(int x, int y, long long val) {
   this->storage[x*N + y] = val;
  }

  long long get(int x, int y) const {
   return this->storage[x*N + y];
  }

  void rmul(const SquareArray* B) {
    for (int i=0; i<N*N; i++) tmp[i] = LLONG_MAX;
    for (int i=0; i<N; i++) for (int j=0; j<N; j++) {
      long long sum = LLONG_MAX;
      for (int k=0; k<N; k++) {
        auto a = storage[i*N+k];
        auto b = B->storage[k*N+j];
        if (a == LLONG_MAX || b == LLONG_MAX) continue;
        sum = min(sum, a + b);
      }
      tmp[i*N + j] = min(tmp[i*N + j], sum);
    }
    swap(tmp, storage);
  }

  void lmul(const SquareArray* B) {
    for (int i=0; i<N*N; i++) tmp[i] = LLONG_MAX;
    for (int i=0; i<N; i++) for (int j=0; j<N; j++) {
      long long sum = LLONG_MAX;
      for (int k=0; k<N; k++) {
        auto a = B->storage[i*N+k];
        auto b = storage[k*N+j];
        if (a == LLONG_MAX || b == LLONG_MAX) continue;
        sum = min(sum, a + b);
      }
      tmp[i*N + j] = min(tmp[i*N + j], sum);
    }
    swap(tmp, storage);
  }

 static SquareArray identity(int n) {
   SquareArray ret = SquareArray(n);
   for (int i=0; i<n; i++) ret.storage[i*n+i] = 0;
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

int N, M, K;

int main() { 
  cin >> N >> M >> K;

  SquareArray adjacency = SquareArray(N);

  for (int i=0; i<M; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    a--; b--;
    adjacency.set(a,b,c);
  }

  adjacency.pow(K);  

  long long ret = LLONG_MAX;

  for (int i=0;i<N; i++) for (int j=0; j<N; j++) {
    ret = min(ret, adjacency.get(i, j));
  }

  if (ret == LLONG_MAX) {
    cout << "IMPOSSIBLE" << endl;
  } else {
    cout << ret << endl;
  }
}
