#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

// testing on https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/B

constexpr int MODULUS = 1000000007;

// Update: scale range (multiply by value)
// Query: range sum
class SegTreeScaleSum {
public:
  unique_ptr<SegTreeScaleSum> lTree;
  unique_ptr<SegTreeScaleSum> rTree;
  i32 leftmost;
  i32 rightmost;

  int total = 0;
  int scale = 1;

  SegTreeScaleSum(vector<int>& a) : SegTreeScaleSum(a, 0, a.size()-1) {}
  SegTreeScaleSum(vector<int>&a, i32 _leftmost, i32 _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      scale = total = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeScaleSum>(new SegTreeScaleSum(a, leftmost, mid));
      rTree = unique_ptr<SegTreeScaleSum>(new SegTreeScaleSum(a, mid+1, rightmost));

      recalc();
    }
  }

  void recalc() {
    if (leftmost == rightmost) {
      this->total = this->scale;
    } else {
      this->total = (lTree->total + rTree->total) * scale;
    }
    this->total %= MODULUS;
  }

  void rangeScale(i32 l, i32 r, int val) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return; }
    // covers
    if (l <= leftmost && rightmost <= r) {
      scale *= val;
      scale %= MODULUS;
      recalc();
      return;
    }
    // delegate to children
    lTree->rangeScale(l, r, val);
    rTree->rangeScale(l, r, val);
    recalc();
  }

  long long rangeSum(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return total; }
    // delegate to children
    return ((lTree->rangeSum(l, r) + rTree->rangeSum(l, r)) * scale) % MODULUS;
  }
};

i32 main() {

  int N, M;
  cin >> N >> M;

  auto arr = vector<int>(N, 1);
  auto st = SegTreeScaleSum(arr);

  while (M --> 0) {
    int t;
    cin >> t;
    if (t == 1) {
      int l, r, v;
      cin >> l >> r >> v;
      st.rangeScale(l, r-1, v);
    } else {
      int l, r;
      cin >> l >> r;
      cout << st.rangeSum(l, r-1) << endl;
    }
  }

  return 0;
}
