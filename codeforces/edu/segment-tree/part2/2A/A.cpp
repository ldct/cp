#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

// tested on https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/A

// Update: increment range
// Query: range minimum
class SegTreeIncrMin {
public:
  unique_ptr<SegTreeIncrMin> lTree;
  unique_ptr<SegTreeIncrMin> rTree;
  i32 leftmost;
  i32 rightmost;

  int minimum = LLONG_MAX;
  int increment = 0;

  SegTreeIncrMin(vector<int>& a) : SegTreeIncrMin(a, 0, a.size()-1) {}
  SegTreeIncrMin(vector<int>&a, i32 _leftmost, i32 _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      increment = minimum = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeIncrMin>(new SegTreeIncrMin(a, leftmost, mid));
      rTree = unique_ptr<SegTreeIncrMin>(new SegTreeIncrMin(a, mid+1, rightmost));

      recalc();
    }
  }

  void recalc() {
    if (leftmost == rightmost) {
      this->minimum = this->increment;
    } else {
      this->minimum = min(lTree->minimum, rTree->minimum) + increment;
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

  long long rangeMin(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return LLONG_MAX; }
    // covers
    if (l <= leftmost && rightmost <= r) { return minimum; }
    // delegate to children
    return min(lTree->rangeMin(l, r), rTree->rangeMin(l, r)) + increment;
  }
};

i32 main() {

  int N, M;
  cin >> N >> M;

  auto arr = vector<int>(N, 0);
  auto st = SegTreeIncrMin(arr);

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
      cout << st.rangeMin(l, r-1) << endl;
    }
  }

  return 0;
}
