#include <bits/stdc++.h>
using namespace std;

class SBool { 
public: 
  bool val;
  SBool (bool _val) { val = _val; } 
  friend ostream& operator << (ostream& os, const SBool& s) { return os << (s.val ? 'Y' : 'N'); } 
  SBool operator+ (const SBool& r) const { return SBool(this->val || r.val); } 
  SBool operator* (const SBool& r) const { return SBool(this->val && r.val); }
  SBool& operator+= (const SBool& r) { this->val = this->val || r.val; return *this; } };

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
        os << s.get(i, j);
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

  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
    int N;
    cin >> N;
    auto adjacency = SquareArray<SBool>(N);
    for (int i=0; i<N; i++) {
      adjacency.set(i, i, SBool(true));
    }
    vector<bool> incoming;
    for (int i=0; i<N; i++) {
      char c;
      cin >> c;
      assert(c == 'Y' || c == 'N');
      if (c == 'Y') {
        incoming.push_back(true);
      } else {
        incoming.push_back(false);
      }
    }

    vector<bool> outgoing;
    for (int i=0; i<N; i++) {
      char c;
      cin >> c;
      assert(c == 'Y' || c == 'N');
      if (c == 'Y') {
        outgoing.push_back(true);
      } else {
        outgoing.push_back(false);
      }
    }

    for (int i=0; i<N; i++) for (int j=0; j<N; j++) {
      if (i == j) {
        adjacency.set(i, j, SBool(true));
        continue;
      }
      if (abs(i - j) != 1) continue; 
      adjacency.set(i, j, SBool(outgoing[i] && incoming[j]));
    }

    adjacency.pow(64);
    cout << "Case #" << t << ": " << endl;
    cout << adjacency;

  }

  return 0;
}
