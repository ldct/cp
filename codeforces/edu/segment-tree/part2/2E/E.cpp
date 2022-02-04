#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

// testing on https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/E

constexpr int NO_OPERATION = LLONG_MAX;

// Update: assign value to range
// Query: range minimum
class SegTreeAssignMin {
public:
  unique_ptr<SegTreeAssignMin> lTree;
  unique_ptr<SegTreeAssignMin> rTree;
  i32 leftmost;
  i32 rightmost;

  int minimum = LLONG_MAX;
  int assigned_val = NO_OPERATION;

  SegTreeAssignMin(vector<int>& a) : SegTreeAssignMin(a, 0, a.size()-1) {}
  SegTreeAssignMin(vector<int>&a, i32 _leftmost, i32 _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      assigned_val = minimum = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeAssignMin>(new SegTreeAssignMin(a, leftmost, mid));
      rTree = unique_ptr<SegTreeAssignMin>(new SegTreeAssignMin(a, mid+1, rightmost));

      recalc();
    }
  }

  void recalc() {
    if (leftmost == rightmost) {
      this->minimum = this->assigned_val;
    } else {
      this->minimum = assigned_val == NO_OPERATION ? min(lTree->minimum, rTree->minimum) : assigned_val;
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

  long long rangeMin(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return LLONG_MAX; }
    // covers
    if (l <= leftmost && rightmost <= r) { return minimum; }
    // delegate to children
    return assigned_val == NO_OPERATION ? min(lTree->rangeMin(l, r), rTree->rangeMin(l, r)) : assigned_val;
  }
};

i32 main() {

  int N, M;
  cin >> N >> M;

  auto arr = vector<int>(N, 0);
  auto st = SegTreeAssignMin(arr);

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
      cout << st.rangeMin(l, r-1) << endl;
    }
  }

  return 0;
}
