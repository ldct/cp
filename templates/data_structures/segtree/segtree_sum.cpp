#include <bits/stdc++.h>
using namespace std;

// ported from SecondThread's Java code

// Update: point set
// Query: range sum
class SegTreeSum {
public:
  unique_ptr<SegTreeSum> lTree;
  unique_ptr<SegTreeSum> rTree;
  int leftmost;
  int rightmost;
  long long total;

  SegTreeSum(vector<long long>& a) : SegTreeSum(a, 0, a.size()-1) {}
  SegTreeSum(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      total = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeSum>(new SegTreeSum(a, leftmost, mid));
      rTree = unique_ptr<SegTreeSum>(new SegTreeSum(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    this->total = lTree->total + rTree->total;
  }

  void pointSet(int idx, long long newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      total = newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  long long rangeSum() { return total; }
  long long rangeSum(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return total; }
    // delegate to children
    return lTree->rangeSum(l, r) + rTree->rangeSum(l, r);
  }

  long long pointGet(int idx) {
    return rangeSum(idx, idx);
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
  auto s = SegTreeSum(A);
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