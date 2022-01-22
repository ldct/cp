#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

class MinPrefixSumTree {
public:
  unique_ptr<MinPrefixSumTree> lTree;
  unique_ptr<MinPrefixSumTree> rTree;
  int leftmost;
  int rightmost;
  int total;
  int smallest_prefix;

  MinPrefixSumTree(vector<int>& a) : MinPrefixSumTree(a, 0, a.size()-1) {}
  MinPrefixSumTree(vector<int>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      total = a[leftmost];
      smallest_prefix = min(0LL, total);
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<MinPrefixSumTree>(new MinPrefixSumTree(a, leftmost, mid));
      rTree = unique_ptr<MinPrefixSumTree>(new MinPrefixSumTree(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    this-> total = lTree->total + rTree->total;
    this->smallest_prefix = min(
      lTree->smallest_prefix,
      lTree->total + rTree->smallest_prefix
    );
  }

  void pointSet(int idx, int newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      total = newVal;
      smallest_prefix = min(0LL, total);
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  int rangeSum(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return total; }
    // delegate to children
    return lTree->rangeSum(l, r) + rTree->rangeSum(l, r);
  }


  int rangeSmallestPrefix(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 200009; }
    // covers
    if (l <= leftmost && rightmost <= r) { return smallest_prefix; }
    // delegate to children
    return min(
      lTree->rangeSmallestPrefix(l, r),
      lTree->rangeSum(l, r) + rTree->rangeSmallestPrefix(l, r)
    );
  }

  string isRBS(int l, int r) {
    if (rangeSum(l, r) != 0) return "No";
    if (rangeSmallestPrefix(l, r) < 0) return "No";
    return "Yes";
  }

  int pointGet(int idx) {
    return rangeSum(idx, idx);
  }
};

int N;
vector<int> arr;
vector<int> tree_arr;

i32 main() {

  cin >> N;
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    arr.push_back(a);
    tree_arr.push_back(0);
  }

  auto segtree = MinPrefixSumTree(tree_arr);
  vector<pair<int, int>> candidates;

  for (int i=0; i<N; i++) {
    if (arr[i] >= 0) {
      segtree.pointSet(i, arr[i]);
    } else {
      candidates.push_back({-arr[i], i});
    }
  }

  sort(candidates.begin(), candidates.end());

  int ret = N;

  for (auto [g, i] : candidates) {
    segtree.pointSet(i, arr[i]);
    if (segtree.rangeSmallestPrefix(0, N-1) < 0) {
      ret--;
      segtree.pointSet(i, 0);
    }
  }

  cout << ret << endl;

  return 0;
}
