#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

// Update: point set
// Query: range sum, Kth one
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

  long long getKth(int k) {
    if (leftmost == rightmost) {
      assert(k == 0);
      return leftmost;
    }
    if (k < lTree->total) return lTree->getKth(k);
    return rTree->getKth(k - lTree->total);
  }
};

int N, M;
vector<int> A;

i32 main() {

  cin >> N >> M;
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A.push_back(a);
  }

  auto st = SegTreeSum(A);
  while (M --> 0) {
    int t, k;
    cin >> t >> k;
    if (t == 1) {
      st.pointSet(k, 1 - st.pointGet(k));
    } else if (t == 2) {
      cout << st.getKth(k) << endl;
    }
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS