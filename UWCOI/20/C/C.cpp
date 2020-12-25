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

int T,N;

int main() {

  cin >> T;

  while (T --> 0) {
    cin >> N;

    vector<long long> idxs;

    for (int i=0; i<N; i++) {
      for (int j=0; j<N; j++) {
        char pos;
        cin >> pos;
        assert(pos == '0' || pos == '1');
        if (pos == '1') { idxs.push_back(j); }
      }
    }

    auto maxTree = SegTree<Max, LLONG_MIN>(idxs);
    auto minTree = SegTree<Min, LLONG_MAX>(idxs);

    long long ret = 0;
    for (int i=0; i<N; i++) {
      for (int j=i; j<N; j++) {
        auto width = maxTree.rangeSum(i, j) - minTree.rangeSum(i, j);
        if (width == (j - i)) {
          ret++;
        }
      }
    }

    cout << ret << endl;
  }


  // vector<long long> a = {0,1,2,3,4};
  // auto s = SegTree<MyMax, LLONG_MIN>(a);
  // cout << s.rangeSum(0, 2) << endl;

  return 0;
}
