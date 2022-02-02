#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

// tested on https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/E

// Update: range increment
// Query: point get
class SegTreeIncr {
public:
  unique_ptr<SegTreeIncr> lTree;
  unique_ptr<SegTreeIncr> rTree;
  i32 leftmost;
  i32 rightmost;
  int increment = 0;

  SegTreeIncr(vector<int>& a) : SegTreeIncr(a, 0, a.size()-1) {}
  SegTreeIncr(vector<int>&a, i32 _leftmost, i32 _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      increment = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeIncr>(new SegTreeIncr(a, leftmost, mid));
      rTree = unique_ptr<SegTreeIncr>(new SegTreeIncr(a, mid+1, rightmost));
    }
  }

  void rangeIncrement(i32 l, i32 r, int val) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return; }
    // covers
    if (l <= leftmost && rightmost <= r) { increment += val; return; }
    // delegate to children
    lTree->rangeIncrement(l, r, val);
    rTree->rangeIncrement(l, r, val);
  }

  int pointGet(i32 idx) {
    if (leftmost == rightmost) return increment;

    int mid = (leftmost + rightmost) / 2;

    if (idx <= mid) {
      return increment + lTree->pointGet(idx);
    } else {
      return increment + rTree->pointGet(idx);
    }
  }
};

i32 main() {

  int N, M;

  cin >> N >> M;

  auto arr = vector<int>(N, 0);
  auto st = SegTreeIncr(arr);

  for (int q=0; q<M; q++) {
    int t;
    cin >> t;
    if (t == 1) {
      int l, r, v;
      cin >> l >> r >> v;
      st.rangeIncrement(l, r-1, v);
    } else {
      int i;
      cin >> i;
      cout << st.pointGet(i) << endl;
    }
  }
}

// DO NOT USE FOR INTERACTIVE PROBLEMS