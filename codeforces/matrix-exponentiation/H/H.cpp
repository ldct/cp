#include <bits/stdc++.h>
using namespace std;

constexpr int MODULUS = 1000000007;

class Mat2Mod {
public:
  long long a,b,c,d;
  Mat2Mod() { a=d=1; b=c=0;}
  Mat2Mod(long long _a, long long _b, long long _c, long long _d) { a=_a%MODULUS;b=_b%MODULUS;c=_c%MODULUS;d=_d%MODULUS; }
  Mat2Mod operator* (const Mat2Mod& r) const { return Mat2Mod(a*r.a+b*r.c, a*r.b+b*r.d, c*r.a+d*r.c, c*r.b+d*r.d); }
};
ostream& operator << (ostream& os, Mat2Mod& m) { return os << "[" << m.a << "," << m.b << ";" << m.c << "," << m.d << "]"; }


class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  Mat2Mod prod;

  SegTree(vector<Mat2Mod>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      prod = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(a, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    this->prod = rTree->prod * lTree->prod;
  }

  void pointSet(int idx, Mat2Mod newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      prod = newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  Mat2Mod rangeProd() { return prod; }
  Mat2Mod rangeProd(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return Mat2Mod(); }
    // covers
    if (l <= leftmost && rightmost <= r) { return prod; }
    // delegate to children
    return rTree->rangeProd(l, r) * lTree->rangeProd(l, r);
  }
};

Mat2Mod mat_of(char c) {
  if (c == 'S' || c == 'D') {
    return Mat2Mod(0, 0, 1, 1);
  } else if (c == 'H') {
    return Mat2Mod(1, 1, 0, 0);
  } else if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
    return Mat2Mod(0, 1, 1, 0);
  } else if (c == '?') {
    return Mat2Mod(19, 6, 7, 20);
  }
  return Mat2Mod();
}

int main() {
  int N, Q;
  cin >> N >> Q;
  string S;
  cin >> S;

  vector<Mat2Mod> a;
  assert(S.size() == N);
  for (int i=0; i<N; i++) {
    a.push_back(mat_of(S[i]));
  }

  SegTree st = SegTree(a, 0, a.size()-1);
  // initial
  auto ss = st.rangeProd(0, a.size()-1);
  cout << ss.a << endl;

  for (int i=0; i<Q; i++) {
    int idx; char c;
    cin >> idx >> c;
    idx--;
    st.pointSet(idx, mat_of(c));
    ss = st.rangeProd(0, a.size()-1);
    cout << ss.a << endl;
  }
    
  return 0;
}
