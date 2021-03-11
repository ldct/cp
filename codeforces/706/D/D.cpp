#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

template<class Op, long long neutral>
class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  long long summary;

  SegTree(vector<long long>& a) : SegTree(a, 0, a.size()-1) {}
  SegTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      summary = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(a, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    Op op;
    this->summary = op(lTree->summary, rTree->summary);
  }

  void pointSet(int idx, long long newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      summary = newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  long long rangeSum() { return summary; }
  long long rangeSum(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return neutral; }
    // covers
    if (l <= leftmost && rightmost <= r) { return summary; }
    // delegate to children
    Op op;
    return op(lTree->rangeSum(l, r), rTree->rangeSum(l, r));
  }

  long long pointGet(int idx) {
    return rangeSum(idx, idx);
  }
  void pointIncrement(int idx, long long amount) {
    Op op;
    pointSet(idx, op(pointGet(idx), amount));
  }
};

// If a maxtree/mintree is needed
struct Max { long long operator()(long long x, long long y) const { return max(x, y); } };
struct Min { long long operator()(long long x, long long y) const { return min(x, y); } };

int N;
vector<int> P, D;

int main() {

  cin >> N;
  for (int i=0; i<N; i++) {
    int p;
    cin >> p;
    P.push_back(p);
  }

  for (int i=0; i<N-1; i++) {
    // 1 -> right
    // -1 -> left
    // for QS
    D.push_back(P[i+1] > P[i] ? 1 : -1);
  }

  vector<int> lpl, lnl;

  if (D[0] == +1) lpl.push_back(1);
  if (D[0] == -1) lpl.push_back(0);
  for (int i=1; i<D.size(); i++) lpl.push_back(D[i] == +1 ? lpl[lpl.size()-1]+1 : 0);

  if (D[0] == +1) lnl.push_back(0);
  if (D[0] == -1) lnl.push_back(1);
  for (int i=1; i<D.size(); i++) lnl.push_back(D[i] == -1 ? lnl[lnl.size()-1]+1 : 0);

  reverse(D.begin(), D.end());

  vector<int> lpr, lnr;
  if (D[0] == +1) lpr.push_back(1);
  if (D[0] == -1) lpr.push_back(0);
  for (int i=1; i<D.size(); i++) lpr.push_back(D[i] == +1 ? lpr[lpr.size()-1]+1 : 0);
  if (D[0] == +1) lnr.push_back(0);
  if (D[0] == -1) lnr.push_back(1);
  for (int i=1; i<D.size(); i++) lnr.push_back(D[i] == -1 ? lnr[lnr.size()-1]+1 : 0);

  reverse(D.begin(), D.end());
  reverse(lpr.begin(), lpr.end());
  reverse(lnr.begin(), lnr.end());

  vector<long long> mt;
  for (int i=0; i<lnr.size(); i++) {
    mt.push_back(max(
      max(lnr[i], lnl[i]),
      max(lpr[i], lpl[i])
    ));
  }
  auto maxtree = SegTree<Max, LLONG_MIN>(mt);

  int ret = 0;
  for (int i=0; i<D.size()-1; i++) {
    int left = lpl[i];
    int right = lnr[i+1];

    int bl = left;
    int br = right;

    if (bl % 2 == 0) bl -= 1;
    if (br % 2 == 0) br -= 1;

    if (bl >= right) continue;
    if (br >= left) continue;

    bl = maxtree.rangeSum(0, i - left-1);
    br = maxtree.rangeSum(i+2+right, mt.size()-1);

    if (max(bl, br) >= max(left, right)) continue;

    ret += 1;
  }

  cout << ret << endl;

  return 0;
}
