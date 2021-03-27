#include <bits/stdc++.h>
using namespace std;

template<class T> ostream& operator << (ostream& os, const vector<T>& v) { for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << " "; } return os; }

int N;
vector<long long> Q;

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

  int T;
  cin >> T;

  while (T --> 0) {
    cin >> N;
    Q.clear();
    for (int i=0; i<N; i++) {
      long long q;
      cin >> q;
      Q.push_back(q);
    }

    vector<long long> ret;
    int last = -1;
    for (const auto q : Q) {
      if (q > last) {
        ret.push_back(q);
        last = q;
      } else {
        ret.push_back(0);
      }
    }

    set<long long> _unused;
    for (int i=1; i<=N; i++) _unused.insert(i);
    for (const auto r : ret) {
      if (r > 0) {
        _unused.erase(r);
      }
    }
    vector<long long> unused;
    for (const auto u : _unused) {
      unused.push_back(u);
    }
    sort(unused.begin(), unused.end());

    auto ret1 = vector<long long>(ret);
    int i=0;
    for (int j=0; j<ret1.size(); j++) {
      if (ret1[j] == 0) {
        ret1[j] = unused[i++];
      }
    }

    cout << ret1 << endl;

    vector<long long> _mt;
    for (int i=0; i<=N; i++) _mt.push_back(i);
    auto mt = SegTree<Max, LLONG_MIN>(_mt);

    last = -1;
    auto ret2 = vector<long long>(ret);
    for (int j=0; j<ret1.size(); j++) {
      if (ret2[j] == 0) {
        assert(last != -1);
        auto r = mt.rangeSum(1, last-1);
        ret2[j] = r;
        mt.pointSet(r, -1);
      } else {
        last = ret2[j];
        mt.pointSet(last, -1);
      }
    }

    cout << ret2 << endl;

  }

  return 0;
}
