#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

// testing on https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/C

// Update(v): a |= v
// Query: range AND
class SegTreeOrAnd {
public:
  unique_ptr<SegTreeOrAnd> lTree;
  unique_ptr<SegTreeOrAnd> rTree;
  i32 leftmost;
  i32 rightmost;

  int or_with = 0;
  int and_summary;

  SegTreeOrAnd(vector<int>& a) : SegTreeOrAnd(a, 0, a.size()-1) {}
  SegTreeOrAnd(vector<int>&a, i32 _leftmost, i32 _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      or_with = and_summary = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeOrAnd>(new SegTreeOrAnd(a, leftmost, mid));
      rTree = unique_ptr<SegTreeOrAnd>(new SegTreeOrAnd(a, mid+1, rightmost));

      recalc();
    }
  }

  void recalc() {
    if (leftmost == rightmost) {
      this->and_summary = this->or_with;
    } else {
      this->and_summary = (lTree->and_summary & rTree->and_summary) | or_with;
    }
  }

  void rangeOrify(i32 l, i32 r, int val) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return; }
    // covers
    if (l <= leftmost && rightmost <= r) {
      or_with |= val;
      recalc();
      return;
    }
    // delegate to children
    lTree->rangeOrify(l, r, val);
    rTree->rangeOrify(l, r, val);
    recalc();
  }

  long long rangeAnd(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return INT_MAX; }
    // covers
    if (l <= leftmost && rightmost <= r) { return and_summary; }
    // delegate to children
    return (lTree->rangeAnd(l, r) & rTree->rangeAnd(l, r)) | or_with;
  }
};

i32 main2() {
  auto arr = vector<int>(4, 0);
  auto st = SegTreeOrAnd(arr);

  st.rangeOrify(0, 2, 3);

  cout << st.rangeAnd(0, 0) << endl;


  // cout << st.or_with << endl;
  // cout << st.lTree->or_with << endl;
  // cout << st.rTree->or_with << endl;

  return 0;
}

i32 main() {

  int N, M;
  cin >> N >> M;

  auto arr = vector<int>(N, 0);
  auto st = SegTreeOrAnd(arr);

  while (M --> 0) {
    int t;
    cin >> t;
    if (t == 1) {
      int l, r, v;
      cin >> l >> r >> v;
      st.rangeOrify(l, r-1, v);
    } else {
      int l, r;
      cin >> l >> r;
      cout << st.rangeAnd(l, r-1) << endl;
    }
  }

  return 0;
}
