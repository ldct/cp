#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

// ported from SecondThread's Java code

using namespace std;

class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  long long minVal;


  SegTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      minVal = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(a, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(a, mid+1, rightmost));

      recalc();
    }
  }

  void recalc() {
    if (leftmost == rightmost) return;
    this->minVal = min(lTree->minVal, rTree->minVal);
  }

  void pointSet(int idx, long long newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      minVal = newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  long long rangeMin(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return LLONG_MAX; }
    // covers
    if (l <= leftmost && rightmost <= r) { return minVal; }
    // delegate to children
    return min(lTree->rangeMin(l, r), rTree->rangeMin(l, r));
  }
};


int main() {

  int T;
  cin >> T;

  for (int t=1; t<=T; t++) {
    long long N, M;
    cin >> N >> M;

    vector<long long> C;

    for (int i=0; i<N; i++) {
      long long c;
      cin >> c;
      if (c == 0) c = LLONG_MAX;
      C.push_back(c);
    }
    // cout << "C=" << C << endl;

    auto _mct = vector<long long>(N, 0);
    auto mct = SegTree(_mct, 0, N-1);

    for (int i=N-2; i != -1; i--) {
      long long min_next_stop = mct.rangeMin(i+1, i+M);
      long long this_cost = C[i];

      if (this_cost == LLONG_MAX || min_next_stop == LLONG_MAX) {
        this_cost = LLONG_MAX;
      } else {
        this_cost += min_next_stop;
      }
      // cout << "set " << i << " " << this_cost << endl;
      mct.pointSet(i, this_cost);
    }

    auto ans = mct.rangeMin(0, M);
    if (ans == LLONG_MAX) {
      ans = -1;
    }
    cout << "Case #" << t << ": " << ans << endl;
  }


  return 0;
}
