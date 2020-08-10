#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

// ported from SecondThread's Java code
class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  long long smin;
  long long min_count;
  long long smax;
  long long max_count;
  long long sum;
  long long square_sum;

  SegTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      sum = smin = smax = a[leftmost];
      square_sum = sum*sum;
      min_count = max_count = 1;
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

    smax = max(lTree->smax, rTree->smax);
    max_count = 0;
    if (smax == lTree->smax) max_count += lTree->max_count;
    if (smax == rTree->smax) max_count += rTree->max_count;

    this->sum = lTree->sum + rTree->sum;
    this->square_sum = lTree->square_sum + rTree->square_sum;
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

  pair<long long, long long> rangeMax(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return { LLONG_MIN, 0 }; }
    // covers
    if (l <= leftmost && rightmost <= r) { return {smax, max_count}; }
    // delegate to children
    auto lp = lTree->rangeMax(l, r);
    auto rp = rTree->rangeMax(l, r);
    auto ret_max = max(lp.first, rp.first);
    auto ret_mc = 0;
    if (ret_max == lp.first) ret_mc += lp.second;
    if (ret_max == rp.first) ret_mc += rp.second;
    return { ret_max, ret_mc };
  }
};

int main() { 
  int N;
  cin >> N;
  vector<long long>A(N, 0);
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A[i] = a;
  }

  auto s = SegTree(A, 0, A.size()-1);


  for (int sqrt_sz=1; sqrt_sz*sqrt_sz<= A.size(); sqrt_sz++) {
    int sz = sqrt_sz*sqrt_sz;
    cout << "testing size " << sz << endl;

    for (int i=0; i<A.size(); i++) {
      int j = i+sz-1;
      auto p = s.rangeMin(i, j);
      if (p.second == sqrt_sz) {
        cout << "the range " << i << " " << j << " is good" << endl;
      }

    }

  }

//   for (int i=0; i<M; i++) {
//     int a, b, c;
//     cin >> a >> b >> c;
//     if (a == 1) {
//       s.pointSet(b, c);
//     } else {
//       auto p = s.rangeMin(b, c-1);
//       cout << p.first << " " << p.second << endl;
//     }
//   }

  return 0;
}
