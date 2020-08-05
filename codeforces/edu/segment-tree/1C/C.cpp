#include <bits/stdc++.h>

// ported from SecondThread's Java code

using namespace std;

class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  long long smin;
  long long min_count;


  SegTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      smin = a[leftmost];
      min_count = 1;
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(a, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    smin = min(lTree->smin, rTree->smin);
    min_count = 0;
    if (smin == lTree->smin) min_count += lTree->min_count;
    if (smin == rTree->smin) min_count += rTree->min_count;
  }

  void pointSet(int idx, int newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      smin = newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  pair<long long, long long> rangeMin(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return { LLONG_MAX, 0 }; }
    // covers
    if (l <= leftmost && rightmost <= r) { return {smin, min_count}; }
    // delegate to children
    auto lp = lTree->rangeMin(l, r);
    auto rp = rTree->rangeMin(l, r);
    auto ret_min = min(lp.first, rp.first);
    auto ret_mc = 0;
    if (ret_min == lp.first) ret_mc += lp.second;
    if (ret_min == rp.first) ret_mc += rp.second;
    return { ret_min, ret_mc };
  }
};

int main() { 
  int N, M;
  cin >> N >> M;
  vector<long long>A(N, 0);
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A[i] = a;
  }
  auto s = SegTree(A, 0, A.size()-1);
  for (int i=0; i<M; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    if (a == 1) {
      s.pointSet(b, c);
    } else {
      auto p = s.rangeMin(b, c-1);
      cout << p.first << " " << p.second << endl;
    }
  }

  return 0;
}
