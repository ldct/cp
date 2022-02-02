#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

// tested on https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/C

constexpr int NO_OPERATION = LLONG_MAX;
// Update: assign value to range
// Query: point get
class SegTreeAssign {
public:
  unique_ptr<SegTreeAssign> lTree;
  unique_ptr<SegTreeAssign> rTree;
  i32 leftmost;
  i32 rightmost;

  int assigned_val = NO_OPERATION;

  SegTreeAssign(vector<int>& a) : SegTreeAssign(a, 0, a.size()-1) {}
  SegTreeAssign(vector<int>&a, i32 _leftmost, i32 _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      assigned_val = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeAssign>(new SegTreeAssign(a, leftmost, mid));
      rTree = unique_ptr<SegTreeAssign>(new SegTreeAssign(a, mid+1, rightmost));
    }
  }

  void prop() {
    if (leftmost == rightmost) return;
    if (assigned_val == NO_OPERATION) return;
    lTree->assigned_val = assigned_val;
    rTree->assigned_val = assigned_val;
    assigned_val = NO_OPERATION;
  }

  void rangeAssign(i32 l, i32 r, int val) {
    prop();
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return; }
    // covers
    if (l <= leftmost && rightmost <= r) { assigned_val = val; return; }
    // delegate to children
    lTree->rangeAssign(l, r, val);
    rTree->rangeAssign(l, r, val);
  }

  int pointGet(i32 idx) {
    if (leftmost == rightmost) return assigned_val;

    int mid = (leftmost + rightmost) / 2;

    if (idx <= mid) {
      return (assigned_val == NO_OPERATION ? lTree->pointGet(idx) : assigned_val);
    } else {
      return (assigned_val == NO_OPERATION ? rTree->pointGet(idx) : assigned_val);
    }
  }
};

i32 main() {

  int N, M;
  cin >> N >> M;

  auto arr = vector<int>(N, 0);
  auto st = SegTreeAssign(arr);

  while (M --> 0) {
    int t;
    cin >> t;
    if (t == 1) {
      int l, r, v;
      cin >> l >> r >> v;
      st.rangeAssign(l, r-1, v);
    } else {
      int i;
      cin >> i;
      cout << st.pointGet(i) << endl;
    }
  }


}

// DO NOT USE FOR INTERACTIVE PROBLEMS