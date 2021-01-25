#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

struct Max { long long operator()(long long x, long long y) const { return max(x, y); } };
struct Min { long long operator()(long long x, long long y) const { return min(x, y); } };

template<typename Op, long long neutral>
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

  int minIdx(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return -1; }
    // covers
    if (leftmost == rightmost) return leftmost;
    if (l <= leftmost && rightmost <= r) {
      if (lTree->rangeSum() < rTree->rangeSum()) {
        return lTree->minIdx(l, r);
      } return rTree->minIdx(l, r);
    }
    // delegate to children
    int a = lTree->minIdx(l, r);
    int b = rTree->minIdx(l, r);

    if (a == -1) return b;
    if (b == -1) return a;

    if (pointGet(a) < pointGet(b)) return a;
    return b;
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

int N;
vector<long long> A;

long long ans(SegTree<Min,LLONG_MAX>& mt, int i, int j) {
  if (i > j) return LLONG_MIN;
  if (i == j) return A[i];
  long long ret = (j - i + 1) * mt.rangeSum(i, j);

  int k = mt.minIdx(i, j);

  assert(i <= k && k <= j);

  ret = max(ret, ans(mt, i, k-1));
  ret = max(ret, ans(mt, k+1, j));

  return ret;
}

int main() {

  cin >> N;

  for (int i=0; i<N; i++) {
    long long a;
    cin >> a;
    A.push_back(a);
  }

  auto minTree = SegTree<Min, LLONG_MAX>(A);

  cout << ans(minTree, 0, A.size()-1) << endl;

  return 0;
}
