#include <bits/stdc++.h>
using namespace std;

// ported from SecondThread's Java code

class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  long long sum;

  // todo: ctor chaining
  // SegTree(vector<long long>& a) { SegTree(a, 0, a.size()-1); }
  SegTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      sum = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(a, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    this->sum = lTree->sum + rTree->sum;
  }

  void pointSet(int idx, int newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      sum = newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  void pointIncrement(int idx, long long newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      sum += newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointIncrement(idx, newVal);
      } else {
        rTree->pointIncrement(idx, newVal);
      }
      recalc();
    }
  }

  long long rangeSum() { return sum; }
  long long rangeSum(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return sum; }
    // delegate to children
    return lTree->rangeSum(l, r) + rTree->rangeSum(l, r);
  }
};

int main() { 
  int N, Q;
  cin >> N >> Q;
  vector<long long>A(N, 0);
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A[i] = a;
  }
  auto s = SegTree(A, 0, A.size()-1);
  for (int i=0; i<Q; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    if (a == 0) {
      s.pointIncrement(b, c);
    } else {
      cout << s.rangeSum(b, c-1) << endl;
    }
  }

  return 0;
}
