#include <bits/stdc++.h>
using namespace std;

class MergeSortTree {
public:
  unique_ptr<MergeSortTree> lTree;
  unique_ptr<MergeSortTree> rTree;
  int leftmost;
  int rightmost;
  map<int, int> freq;

  MergeSortTree(vector<long long>& a) : MergeSortTree(a, 0, a.size()-1) {}
  MergeSortTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      freq = map<int, int>();
      freq[a[leftmost]] = 1;
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<MergeSortTree>(new MergeSortTree(a, leftmost, mid));
      rTree = unique_ptr<MergeSortTree>(new MergeSortTree(a, mid+1, rightmost));

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

  int rangeFreq(long long ofElement) { return freq[ofElement]; }
  int rangeFreq(long long ofElement, int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return freq[ofElement]; }
    // delegate to children
    return lTree->rangeFreq(ofElement, l, r) + rTree->rangeFreq(ofElement, l, r);
  }
};

int main() {
  int N, Q;
  cin >> N >> Q;
  vector<long long>A(N, 0);
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A[i] = a;
  }
  auto s = MergeSortTree(A);
  for (int i=0; i<Q; i++) {
    int a, b, c;
    cin >> a >> b >> c;
    if (a == 0) {
      s.pointIncrement(b, c);
    } else {
      cout << s.rangeSum(b, c-1) << endl;
    }
  }

  return 0;
}
