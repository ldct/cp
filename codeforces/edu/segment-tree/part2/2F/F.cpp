#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

// testing on https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/F

constexpr int NO_OPERATION = LLONG_MAX;

// Update: assign value to range
// Query: range sum
class SegTreeAssignSum {
public:
  unique_ptr<SegTreeAssignSum> lTree;
  unique_ptr<SegTreeAssignSum> rTree;
  i32 leftmost;
  i32 rightmost;

  int total = 0;
  int assigned_val = NO_OPERATION;

  SegTreeAssignSum(vector<int>& a) : SegTreeAssignSum(a, 0, a.size()-1) {}
  SegTreeAssignSum(vector<int>&a, i32 _leftmost, i32 _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      assigned_val = total = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeAssignSum>(new SegTreeAssignSum(a, leftmost, mid));
      rTree = unique_ptr<SegTreeAssignSum>(new SegTreeAssignSum(a, mid+1, rightmost));

      recalc();
    }
  }

  int sz() {
    return rightmost - leftmost + 1;
  }

  void recalc() {
    if (leftmost == rightmost) {
      this->total = this->assigned_val;
    } else {
      this->total = assigned_val == NO_OPERATION ? (lTree->total + rTree->total) : assigned_val * sz();
    }
  }

  void prop() {
    if (leftmost == rightmost) return;
    if (assigned_val == NO_OPERATION) return;
    lTree->assigned_val = assigned_val;
    rTree->assigned_val = assigned_val;
    lTree->recalc();
    rTree->recalc();
    assigned_val = NO_OPERATION;
  }

  void rangeAssign(i32 l, i32 r, int val) {
    prop();
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return; }
    // covers
    if (l <= leftmost && rightmost <= r) {
      assigned_val = val;
      recalc();
      return;
    }
    // delegate to children
    lTree->rangeAssign(l, r, val);
    rTree->rangeAssign(l, r, val);
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
    return assigned_val == NO_OPERATION ? lTree->rangeSum(l, r) + rTree->rangeSum(l, r) :  assigned_val * (rr - ll + 1);
  }
};

i32 main() {

  int N, M;
  cin >> N >> M;

  auto arr = vector<int>(N, 0);
  auto st = SegTreeAssignSum(arr);

  while (M --> 0) {
    int t;
    cin >> t;
    if (t == 1) {
      int l, r, v;
      cin >> l >> r >> v;
      st.rangeAssign(l, r-1, v);
    } else {
      int l, r;
      cin >> l >> r;
      cout << st.rangeSum(l, r-1) << endl;
    }
  }

  return 0;
}
