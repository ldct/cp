#include <bits/stdc++.h>
using namespace std;

// ported from SecondThread's Java code

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

// If a maxtree/mintree is needed
struct Max { long long operator()(long long x, long long y) const { return max(x, y); } };
struct Min { long long operator()(long long x, long long y) const { return min(x, y); } };


int main() {
  int N, Q;
  cin >> N >> Q;
  vector<long long>A(N, 0);
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A[i] = a;
  }
  auto s = SegTree<plus<long long>, 0>(A);
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

/// This is somewhat faster

struct BIT {
	vector<long long> s;
	BIT(int n) : s(n) {}
	void pointSet(int pos, long long dif) { // a[pos] += dif
		for (; pos < s.size(); pos |= pos + 1) s[pos] += dif;
	}
	long long rangeSum(int pos) { // sum of values in [0, pos)
		long long res = 0;
		for (; pos > 0; pos &= pos - 1) res += s[pos-1];
		return res;
	}
};