#include <bits/stdc++.h>
using namespace std;

typedef struct _Summary {
  int a, b, c, ab, bc, abc;
  _Summary(int _a, int _b, int _c, int _ab, int _bc, int _abc) {
    a = _a; b = _b, c = _c; ab = _ab; bc = _bc; abc = _abc;
  }
} Summary;

Summary zero() {
  return _Summary(0, 0, 0, 0, 0, 0);
}

Summary merge(Summary l, Summary r) {
  return Summary(
    l.a + r.a,
    l.b + r.b,
    l.c + r.c,
    min(l.a + r.ab, l.ab + r.b),
    min(l.b + r.bc, l.bc + r.c),
    min(
      l.ab + r.bc,
      min(
        l.abc + r.c,
        l.a + r.abc
      )
    )
  );
}

Summary root(char c) {
  if (c == 'a') return Summary(1, 0, 0, 0, 0, 0);
  if (c == 'b') return Summary(0, 1, 0, 0, 0, 0);
  if (c == 'c') return Summary(0, 0, 1, 0, 0, 0);
  assert(false);
}

class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  Summary summary = zero();

  SegTree(string& str) : SegTree(str, 0, str.size()-1) {}
  SegTree(string& str, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      summary = root(str[leftmost]);
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(str, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(str, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    this->summary = merge(lTree->summary, rTree->summary);
  }

  void pointSet(int idx, char newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      summary = root(newVal);
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  Summary rangeSum() { return summary; }
  Summary rangeSum(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return zero(); }
    // covers
    if (l <= leftmost && rightmost <= r) { return summary; }
    // delegate to children
    return merge(lTree->rangeSum(l, r), rTree->rangeSum(l, r));
  }
};

int main() {

  int N, Q;
  cin >> N >> Q;
  string S;
  cin >> S;
  auto tree = SegTree(S);

  while (Q --> 0) {
    int pos;
    char c;
    cin >> pos >> c;
    pos--;
    tree.pointSet(pos, c);
    cout << tree.summary.abc << endl;
  }



  return 0;
}
