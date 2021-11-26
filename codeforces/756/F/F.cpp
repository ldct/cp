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

int T;
int N, S;
vector<long long> A;

class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  long long _min;

  SegTree(vector<long long>& a) : SegTree(a, 0, a.size()-1) {}
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

bool ok(SegTree& st, int l, int r) {
  return -st.rangeMin(l, l) + st.rangeMin(l, r) + S >= 0;
}

int ans(SegTree& st, int l) {
  int low = l;
  int high = N;

  if (!ok(st, l, low)) return -1;
  if (ok(st, l, high)) return high;

  while (high - low > 1) {
    int mid = (low + high) / 2;
    if (ok(st, l, mid)) {
      low = mid;
    } else {
      high = mid;
    }
  }

  for (int i=low; i<= high; i++) {
    if (!ok(st, l, i)) return i-1;
  }

  assert(false);
  return 0;

}
int main() {

  cin >> T;
  while (T --> 0) {
    A.clear();
    cin >> N >> S;
    A.push_back(0);
    for (int i=0; i<N; i++) {
      int a;
      cin >> a;
      A.push_back(A[A.size()-1] + a);
    }

    // cout << A << endl;
    auto st = SegTree(A);

    int best = 0;
    int bl = -1;
    int br = -1;

    for (int l = 0; l<N; l++) {
      int r = ans(st, l);
      if (r == -1) continue;
      int candidate = r-l+1;
      if (candidate > best) {
        best = candidate;
        bl = l; br = r;
      }
    }
    bl++; best--;
    if (best == 0) {
      cout << -1 << endl;
    } else {
      cout << bl << " " << br << endl;
    }
  }

  return 0;
}
