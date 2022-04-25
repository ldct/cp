#include <bits/stdc++.h>
using namespace std;

// TLE on https://judge.yosupo.jp/problem/static_range_frequency
// 2.5s to construct the tree for 2e5 elements

class SegTreeFreq {
public:
  unique_ptr<SegTreeFreq> lTree;
  unique_ptr<SegTreeFreq> rTree;
  int leftmost;
  int rightmost;
  map<int, int> freq;

  SegTreeFreq(vector<long long>& a) : SegTreeFreq(a, 0, a.size()-1) {}
  SegTreeFreq(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      freq = map<int, int>();
      freq[a[leftmost]] = 1;
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeFreq>(new SegTreeFreq(a, leftmost, mid));
      rTree = unique_ptr<SegTreeFreq>(new SegTreeFreq(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    freq = map<int, int>(lTree->freq);
    for (auto p : rTree->freq) freq[p.first] += p.second;
  }

//   void pointSet(int idx, long long newVal) {
//     if (leftmost == rightmost && leftmost == idx) {
//       summary = newVal;
//     } else {
//       if (idx <= lTree->rightmost) {
//         lTree->pointSet(idx, newVal);
//       } else {
//         rTree->pointSet(idx, newVal);
//       }
//       recalc();
//     }
//   }

  int rangeFreq(long long target) { return freq[target]; }
  int rangeFreq(long long target, int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return freq[target]; }
    // delegate to children
    return lTree->rangeFreq(target, l, r) + rTree->rangeFreq(target, l, r);
  }
};

int main() {

  int N, Q;
  cin >> N >> Q;
  vector<long long> arr;
  while (N --> 0) {
    long long a;
    cin >> a;
    arr.push_back(a);
  }
  auto engine = SegTreeFreq(arr);
  cout << "done" << endl; return 0;
  while (Q --> 0) {
    int l, r, x;
    cin >> l >> r >> x;
    cout << engine.rangeFreq(x, l, r-1) << endl;
  }

  return 0;
}