#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

// tested on https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/B

constexpr int NO_OPERATION = LLONG_MIN;
// Update(v): a := max(a, v) in range
// Query: point get
class SegTreeMaximize {
public:
  unique_ptr<SegTreeMaximize> lTree;
  unique_ptr<SegTreeMaximize> rTree;
  i32 leftmost;
  i32 rightmost;

  int max_with = NO_OPERATION;

  SegTreeMaximize(vector<int>& a) : SegTreeMaximize(a, 0, a.size()-1) {}
  SegTreeMaximize(vector<int>&a, i32 _leftmost, i32 _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      max_with = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeMaximize>(new SegTreeMaximize(a, leftmost, mid));
      rTree = unique_ptr<SegTreeMaximize>(new SegTreeMaximize(a, mid+1, rightmost));
    }
  }

  void prop() {
    if (leftmost == rightmost) return;
    if (max_with == NO_OPERATION) return;
    lTree->max_with = max(lTree->max_with, max_with);
    rTree->max_with = max(rTree->max_with, max_with);
    max_with = NO_OPERATION;
  }

  void rangeMaximize(i32 l, i32 r, int val) {
    prop();
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return; }
    // covers
    if (l <= leftmost && rightmost <= r) { max_with = max(max_with, val); return; }
    // delegate to children
    lTree->rangeMaximize(l, r, val);
    rTree->rangeMaximize(l, r, val);
  }

  int pointGet(i32 idx) {
    if (leftmost == rightmost) return max_with;

    int mid = (leftmost + rightmost) / 2;

    if (idx <= mid) {
      return (max_with == NO_OPERATION ? lTree->pointGet(idx) : max(max_with, lTree->pointGet(idx)));
    } else {
      return (max_with == NO_OPERATION ? rTree->pointGet(idx) : max(max_with, rTree->pointGet(idx)));
    }
  }

  void dump() {
    cout << "(" << leftmost << "," << rightmost << ") " << max_with << endl;
    if (lTree) lTree->dump();
    if (rTree) rTree->dump();
  }
};

i32 main2() {
  auto arr = vector<int>(4, 0);
  auto st = SegTreeMaximize(arr);

  st.rangeMaximize(0, 1, 5);
  st.rangeMaximize(1, 2, 3);

  st.dump();

  for (int i=0; i<arr.size(); i++) {
    cout << st.pointGet(i) << endl;
  }

  return 0;
}

i32 main() {

  int N, M;
  cin >> N >> M;

  auto arr = vector<int>(N, 0);
  auto st = SegTreeMaximize(arr);

  while (M --> 0) {
    int t;
    cin >> t;
    if (t == 1) {
      int l, r, v;
      cin >> l >> r >> v;
      st.rangeMaximize(l, r-1, v);
    } else {
      int i;
      cin >> i;
      cout << st.pointGet(i) << endl;
    }
  }

  return 0;
}
