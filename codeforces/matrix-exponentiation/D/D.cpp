#include <bits/stdc++.h>
using namespace std;

constexpr int MODULUS = 1000000007;

template<typename numeric_t = long long, numeric_t MODULUS = MODULUS> class RInt { public: numeric_t val; RInt (numeric_t _val) { val = _val; } friend ostream& operator << (ostream& os, const RInt& s) { return os << s.val; } RInt operator+ (const RInt& r) const { return RInt((this->val + r.val) % MODULUS); } RInt operator* (const RInt& r) const { return RInt((this->val * r.val) % MODULUS); } RInt& operator+= (const RInt& r) { this->val += r.val; this->val %= MODULUS; return *this; } };

template<typename numeric_t>
class SquareArray {
public:
  vector<numeric_t> storage;
  vector<numeric_t> tmp;
  int N;

  SquareArray(int N) {
    this->N = N;
    this->storage = vector<numeric_t>(N*N, 0);
    this->tmp = vector<numeric_t>(N*N, 0);
  }

  friend vector<numeric_t> operator * (const SquareArray& s, const vector<numeric_t>v) {
    vector<numeric_t> ret;
    for (int i=0; i<s.N; i++) {
      numeric_t sum = 0;
      for (int j=0; j<s.N; j++) {
        sum += s.get(i, j)*v[j];
      }
      ret.push_back(sum);
    }
    return ret;
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

  void set(int x, int y, numeric_t val) {
   this->storage[x*N + y] = val;
  }

  numeric_t get(int x, int y) const {
   return this->storage[x*N + y];
  }

 void rmul(const SquareArray* B) {
   for (int i=0; i<N*N; i++) tmp[i] = 0;
   for (int i=0; i<N; i++) for (int j=0; j<N; j++) for (int k=0; k<N; k++) {
     tmp[i*N + k] += (storage[i*N+j]*B->storage[j*N+k]);
   }
   swap(tmp, storage);
 }

  void lmul(const SquareArray* B) {
   for (int i=0; i<N*N; i++) tmp[i] = 0;
   for (int i=0; i<N; i++) for (int j=0; j<N; j++) for (int k=0; k<N; k++) {
     tmp[i*N + k] += (B->storage[i*N+j]*storage[j*N+k]);
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
  int N, M, K;
  cin >> N >> M >> K;
  auto adjacency = SquareArray<RInt<>>(N);

  for (int i=0; i<M; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    adjacency.set(a, b, 1);
  }

  adjacency.pow(K);

  auto ret = RInt<>(0);

  for (int i=0; i<N; i++) for (int j=0; j<N; j++) {
    ret += adjacency.storage[i*N+j];
  }

  cout << ret << endl;

  return 0;
}
