#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }


class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  long long _min;

  // todo: ctor chaining
  // SegTree(vector<long long>& a) { SegTree(a, 0, a.size()-1); }
  SegTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      this->_min = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(a, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    this->_min = min(lTree->_min, rTree->_min);
  }

  void pointSet(int idx, int newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      _min = newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  long long rangeMin() { return _min; }
  long long rangeMin(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return LLONG_MAX; }
    // covers
    if (l <= leftmost && rightmost <= r) { return this->_min; }
    // delegate to children
    return min(lTree->rangeMin(l, r), rTree->rangeMin(l, r));
  }
};

int T;

int main() {

  cin >> T;
  while (T --> 0) {
    int N;
    cin >> N;
    vector<long long> A;
    for (int i=0; i<N; i++) {
      long long a;
      cin >> a;
      A.push_back(a);
    }

    auto s = SegTree(A, 0, A.size()-1);

    int start = 0;
    int end = N-1;

    long long maxStart = A[start];
    long long maxEnd = A[end];

    while (start < end) {
      // vector<long long> v = {start, maxStart, end, maxEnd, s.rangeMin(start+1, end-1)};
      // cout << v << endl;
      if (maxStart == maxEnd) {
        if (s.rangeMin(start+1, end-1) == maxStart) {
          cout << "YES" << endl;
          break;
        } else {
          if (A[start+1] < maxStart) {
            start += 1;
          } else {
            end -= 1;
            maxEnd = max(maxEnd, A[end]);
          }
        }
      } else if (maxStart < maxEnd) {
        start += 1;
        maxStart = max(maxStart, A[start]);
      } else if (maxStart > maxEnd) {
        end -= 1;
        maxEnd = max(maxEnd, A[end]);
      } else {
        assert(false);
      }
    }

    if (start < end) {
      int x = start + 1;
      int y = end - start - 1;
      int z = A.size() - x - y;

      assert(x > 0);
      assert(y > 0);
      assert(z > 0);
      cout << x << " " << y << " " << A.size() - x - y << endl;
    } else {
      cout << "NO" << endl;
    }

  }
  return 0;
}
