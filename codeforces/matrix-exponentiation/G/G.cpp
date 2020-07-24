#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

constexpr long long MODULUS = 1000000007;

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

  friend vector<long long> operator * (const SquareArray& s, const vector<long long>v) {
    vector<long long> ret;
    for (int i=0; i<s.N; i++) {
      long long sum = 0;
      for (int j=0; j<s.N; j++) {
        sum += s.get(i, j)*v[j];
        sum %= MODULUS;
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

  void set(int x, int y, long long val) {
   this->storage[x*N + y] = val;
  }

  long long get(int x, int y) const {
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

  long long N, K;
  cin >> N >> K;

  SquareArray adjacency = SquareArray(N+3);

  vector<long long> A, AA;

  for (int i=0; i<N; i++) {
    long long a;
    cin >> a;
    A.push_back(a);
    AA.push_back(a);
  }
  reverse(A.begin(), A.end());
  A.push_back(N*N);
  A.push_back(N);
  A.push_back(1);

  for (int i=0; i<N; i++) {
    long long c;
    cin >> c;
    adjacency.set(0, i, c);
  }

  for (int i=0; i<N-1; i++) {
    adjacency.set(i+1,i, 1);
  }

  adjacency.set(N, N+0, 1);
  adjacency.set(N, N+1, 2);
  adjacency.set(N, N+2, 1);

  adjacency.set(N+1, N+1, 1);
  adjacency.set(N+1, N+2, 1);

  adjacency.set(N+2, N+2, 1);

  long long p,q,r;
  cin >> p >> q >> r;

  adjacency.set(0, N+0, r);
  adjacency.set(0, N+1, q);
  adjacency.set(0, N+2, p);

  // cout << adjacency << endl;

  if (K-N+1 < 0) {
    cout << AA[K] << endl;
    return 0;
  }

  adjacency.pow(K-N+1);
  cout << (adjacency*A)[0] << endl;
  
  // cout << adjacency << endl;

  // cout << A << endl;
  // cout << adjacency*A << endl;

  // for (int i=0; i<65; i++) {
  //   for (int j=0; j<65; j++) {
  //     cout << adjacency.get(i, j) << " ";
  //   }
  //   cout << endl;
  // }

}
