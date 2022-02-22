#include <bits/stdc++.h>

// ported from SecondThread's Java code

using namespace std;

class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  long long smin;


  SegTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      smin = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(a, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    this->smin = min(lTree->smin, rTree->smin);
  }

  void pointSet(int idx, int newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      smin = newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  long long rangeMin(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return LLONG_MAX; }
    // covers
    if (l <= leftmost && rightmost <= r) { return smin; }
    // delegate to children
    return min(lTree->rangeMin(l, r), rTree->rangeMin(l, r));
  }
};

int main() { 
  int N, M;
  cin >> N >> M;
  vector<long long>A(N, 0);
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A[i] = a;
  }
  auto s = SegTree(A, 0, A.size()-1);
  for (int i=0; i<M; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    if (a == 1) {
      s.pointSet(b, c);
    } else {
      cout << s.rangeMin(b, c-1) << endl;
    }
  }

  return 0;
}
