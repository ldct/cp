#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

// testing on https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/D

// Update: increment range
// Query: range sum
class SegTreeIncrSum {
public:
  unique_ptr<SegTreeIncrSum> lTree;
  unique_ptr<SegTreeIncrSum> rTree;
  i32 leftmost;
  i32 rightmost;

  int increment = 0;
  int total = 0;

  SegTreeIncrSum(vector<int>& a) : SegTreeIncrSum(a, 0, a.size()-1) {}
  SegTreeIncrSum(vector<int>&a, i32 _leftmost, i32 _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      increment = total = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeIncrSum>(new SegTreeIncrSum(a, leftmost, mid));
      rTree = unique_ptr<SegTreeIncrSum>(new SegTreeIncrSum(a, mid+1, rightmost));

      recalc();
    }
  }

  int sz() {
    return rightmost - leftmost + 1;
  }

  void recalc() {
    if (leftmost == rightmost) {
      this->total = this->increment;
    } else {
      this->total = lTree->total + rTree->total + increment*sz();
    }
  }

  void rangeIncrement(i32 l, i32 r, int val) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return; }
    // covers
    if (l <= leftmost && rightmost <= r) {
      increment += val;
      recalc();
      return;
    }
    // delegate to children
    lTree->rangeIncrement(l, r, val);
    rTree->rangeIncrement(l, r, val);
    recalc();
  }

  long long rangeSum(i32 l, i32 r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return total; }
    // delegate to children
    auto ll = max(leftmost, l);
    auto rr = min(rightmost, r);
    return lTree->rangeSum(l, r) + rTree->rangeSum(l, r) + increment * (rr - ll + 1);
  }
};

i32 main2() {
  auto arr = vector<int>(4, 0);
  auto st = SegTreeIncrSum(arr);

  st.rangeIncrement(0, 2, 3);
  st.rangeIncrement(1, 3, 4);

  cout << st.rangeSum(1, 2) << endl;
  cout << st.total << endl;

  return 0;
}

i32 main() {

  int N, M;
  cin >> N >> M;

  auto arr = vector<int>(N, 0);
  auto st = SegTreeIncrSum(arr);

  while (M --> 0) {
    int t;
    cin >> t;
    if (t == 1) {
      int l, r, v;
      cin >> l >> r >> v;
      st.rangeIncrement(l, r-1, v);
    } else {
      int l, r;
      cin >> l >> r;
      cout << st.rangeSum(l, r-1) << endl;
    }
  }

  return 0;
}
