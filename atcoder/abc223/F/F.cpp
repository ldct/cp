#include <bits/stdc++.h>
using namespace std;

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  long long total;
  long long smallest_prefix;

  SegTree(vector<long long>& a) : SegTree(a, 0, a.size()-1) {}
  SegTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      total = a[leftmost];
      smallest_prefix = min(0LL, total);
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(a, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(a, mid+1, rightmost));

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

  void pointSet(int idx, long long newVal) {
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

  long long rangeSum(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return total; }
    // delegate to children
    return lTree->rangeSum(l, r) + rTree->rangeSum(l, r);
  }


  long long rangeSmallestPrefix(int l, int r) {
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

  long long pointGet(int idx) {
    return rangeSum(idx, idx);
  }
};

int N, Q;
string S;

int main() {

  cin >> N >> Q;
  cin >> S;

  vector<long long> points;
  for (auto s : S) {
    if (s == '(') {
      points.push_back(1);
    } else if (s == ')') {
      points.push_back(-1);
    } else {
      assert(false);
    }
  }

  // cout << "points=" << points << endl;

  auto tree = SegTree(points);


  for (int i=0; i<Q; i++) {
    int t, l, r;
    cin >> t >> l >> r;
    l--; r--;
    if (t == 1) {
      int old_l = tree.pointGet(l);
      int old_r = tree.pointGet(r);
      tree.pointSet(l, old_r);
      tree.pointSet(r, old_l);
    } else if (t == 2) {
      cout << tree.isRBS(l, r) << endl;
    } else {
      assert(false);
    }
  }

  return 0;
}
