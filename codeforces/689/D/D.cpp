#include <bits/stdc++.h>
using namespace std;

using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

class SumTree {
public:
  unique_ptr<SumTree> lTree;
  unique_ptr<SumTree> rTree;
  int leftmost;
  int rightmost;
  long long sum;

  SumTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      sum = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SumTree>(new SumTree(a, leftmost, mid));
      rTree = unique_ptr<SumTree>(new SumTree(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    this->sum = lTree->sum + rTree->sum;
  }

  void pointSet(int idx, int newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      sum = newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  void pointIncrement(int idx, long long newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      sum += newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointIncrement(idx, newVal);
      } else {
        rTree->pointIncrement(idx, newVal);
      }
      recalc();
    }
  }

  long long rangeSum() { return sum; }
  long long rangeSum(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return sum; }
    // delegate to children
    return lTree->rangeSum(l, r) + rTree->rangeSum(l, r);
  }
};

int T;
int N, Q;
vector<long long> A;
set<long long> valid_sums;

void process(int start, int end, SumTree& sumTree) {
  if (!(start <= end)) return;
  valid_sums.insert(sumTree.rangeSum(start, end));
  if (start == end) return;

  long long mid = (A[start] + A[end]) / 2;
  int i = upper_bound(A.begin(), A.end(), mid) - A.begin();

  if (i-1 != end) process(start, i-1, sumTree);
  if (i != start) process(i, end, sumTree);
}

int main() {

  cin >> T;

  while (T --> 0) {
    cin >> N >> Q;
    A.clear();
    valid_sums.clear();

    for (int i=0; i<N; i++) {
      long long a;
      cin >> a;
      A.push_back(a);
    }

    sort(A.begin(), A.end());
    auto sumTree = SumTree(A, 0, A.size()-1);
    // cout << A << endl;

    sumTree = SumTree(A, 0, A.size()-1);

    process(0, A.size()-1, sumTree);
    // cout << valid_sums << endl;

    for (int i=0; i<Q; i++) {
      int q;
      cin >> q;
      if (valid_sums.count(q) == 0) {
        cout << "No" << endl;
      } else {
        cout << "Yes" << endl;
      }
    }
  }

  return 0;
}
