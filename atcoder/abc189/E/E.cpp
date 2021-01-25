#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

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

  SquareArray clone() {
    SquareArray ret(N);
    for (int i=0; i<N; i++) for (int j=0; j<N; j++) {
      ret.set(i, j, this->get(i, j));
    }
    return ret;
  }

  friend vector<long long> operator * (const SquareArray& s, const vector<long long>v) {
    vector<long long> ret;
    for (int i=0; i<s.N; i++) {
      long long sum = 0;
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

  void set(int x, int y, long long val) {
   this->storage[x*N + y] = val;
  }

  long long get(int x, int y) const {
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

};

auto mat1 = SquareArray(3);
auto mat2 = SquareArray(3);
auto pure_flipx = SquareArray(3);
auto pure_flipy = SquareArray(3);

SquareArray translate(long long x, long long y) {
  auto ret = SquareArray(3);

  ret.set(0, 0, 1);
  ret.set(1, 1, 1);
  ret.set(2, 2, 1);

  ret.set(0, 2, x);
  ret.set(1, 2, y);

  return ret;
}

SquareArray flipx(long long p) {
  auto ret = translate(-p, 0);
  ret.lmul(&pure_flipx);
  auto tmp = translate(p, 0);
  ret.lmul(&tmp);

  return ret;
}

SquareArray flipy(long long p) {
  auto ret = translate(0, -p);
  ret.lmul(&pure_flipy);
  auto tmp = translate(0, p);
  ret.lmul(&tmp);

  return ret;
}


int N, M, Q;

int main() {

  mat1.set(0, 1, 1);
  mat1.set(1, 0, -1);
  mat1.set(2, 2, 1);

  mat2.set(0, 1, -1);
  mat2.set(1, 0, 1);
  mat2.set(2, 2, 1);

  pure_flipx.set(0, 0, -1);
  pure_flipx.set(1, 1, 1);
  pure_flipx.set(2, 2, 1);

  pure_flipy.set(0, 0, 1);
  pure_flipy.set(1, 1, -1);
  pure_flipy.set(2, 2, 1);

  cin >> N;
  vector<vector<long long>> points;
  for (int i=0; i<N; i++) {
    long long x, y;
    cin >> x >> y;
    vector<long long> p = {x, y, 1};
    points.push_back(p);
  }

  cin >> M;
  auto ti = SquareArray::identity(3);
  vector<SquareArray> transforms;
  transforms.push_back(ti);
  for (int i=0; i<M; i++) {
    int op;
    cin >> op;
    SquareArray t = transforms[transforms.size()-1].clone();
    if (op == 1) {
      t.lmul(&mat1);
    } else if (op == 2) {
      t.lmul(&mat2);
    } else if (op == 3) {
      long long  p;
      cin >> p;
      auto tmp = flipx(p);
      t.lmul(&tmp);
    } else if (op == 4) {
      long long  p;
      cin >> p;
      auto tmp = flipy(p);
      t.lmul(&tmp);
    } else { assert(false); }
    transforms.push_back(t);
  }
  // cout << transforms << endl;

  cin >> Q;
  for (int i=0; i<Q; i++) {
    int a, b;
    cin >> a >> b;
    b--;
    auto v = transforms[a] * points[b];
    cout << v[0] << " " << v[1] << endl;
  }

  return 0;
}
