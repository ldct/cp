#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

// XOR segment tree class SegTreeXOR
template<class Op, long long neutral>
class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  long long summary;

  SegTree(vector<long long>& a) : SegTree(a, 0, a.size()-1) {}
  SegTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      summary = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(a, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    Op op;
    this->summary = op(lTree->summary, rTree->summary);
  }

  void pointSet(int idx, long long newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      summary = newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  long long rangeSum() { return summary; }
  long long rangeSum(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return neutral; }
    // covers
    if (l <= leftmost && rightmost <= r) { return summary; }
    // delegate to children
    Op op;
    return op(lTree->rangeSum(l, r), rTree->rangeSum(l, r));
  }

  long long pointGet(int idx) {
    return rangeSum(idx, idx);
  }
  void pointIncrement(int idx, long long amount) {
    Op op;
    pointSet(idx, op(pointGet(idx), amount));
  }
};

int N, Q;
int main() {
  cin >> N >> Q;
  vector<long long>A(N, 0);
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A[i] = a;
  }

  auto x = SegTree<bit_xor<long long>, 0>(A);

  for (int i=0; i<Q; i++) {
    long long T, X, Y;
    cin >> T >> X >> Y;
    X--; Y--;
    if (T == 1) {
      x.pointIncrement(X, Y+1);
    } else {
      cout << x.rangeSum(X, Y) << endl;
    }
  }

  return 0;
}