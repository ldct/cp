#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

constexpr int NO_OPERATION = LLONG_MAX;

// Update: assign value to range
// Query: range sum
class SegTreeAssignSum {
public:
  unique_ptr<SegTreeAssignSum> lTree;
  unique_ptr<SegTreeAssignSum> rTree;
  i32 leftmost;
  i32 rightmost;

  int total = 0;
  int assigned_val = NO_OPERATION;

  SegTreeAssignSum(vector<int>& a) : SegTreeAssignSum(a, 0, a.size()-1) {}
  SegTreeAssignSum(vector<int>&a, i32 _leftmost, i32 _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      assigned_val = total = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeAssignSum>(new SegTreeAssignSum(a, leftmost, mid));
      rTree = unique_ptr<SegTreeAssignSum>(new SegTreeAssignSum(a, mid+1, rightmost));

      recalc();
    }
  }

  int sz() {
    return rightmost - leftmost + 1;
  }

  void recalc() {
    if (leftmost == rightmost) {
      this->total = this->assigned_val;
    } else {
      this->total = assigned_val == NO_OPERATION ? (lTree->total + rTree->total) : assigned_val * sz();
    }
  }

  void prop() {
    if (leftmost == rightmost) return;
    if (assigned_val == NO_OPERATION) return;
    lTree->assigned_val = assigned_val;
    rTree->assigned_val = assigned_val;
    lTree->recalc();
    rTree->recalc();
    assigned_val = NO_OPERATION;
  }

  void rangeAssign(i32 l, i32 r, int val) {
    prop();
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return; }
    // covers
    if (l <= leftmost && rightmost <= r) {
      assigned_val = val;
      recalc();
      return;
    }
    // delegate to children
    lTree->rangeAssign(l, r, val);
    rTree->rangeAssign(l, r, val);
    recalc();
  }

  long long rangeSum(i32 l, i32 r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return total; }
    // delegate to children
    auto ll = max(leftmost, l);
    auto rr = min(rightmost, r);
    return assigned_val == NO_OPERATION ? lTree->rangeSum(l, r) + rTree->rangeSum(l, r) :  assigned_val * (rr - ll + 1);
  }
};

int N, Q, X;

SegTreeAssignSum* lt;
SegTreeAssignSum* gt;
int pos_X;

void assign_block(SegTreeAssignSum* st, i32 l, i32 r, i32 num_first, int v0, int v1) {
  st->rangeAssign(l, l + num_first - 1, v0);
  st->rangeAssign(l + num_first, r, v1);
}

void sort_ascending(int l, int r) {
  int num_lt = lt->rangeSum(l, r);
  int num_gt = gt->rangeSum(l, r);

  if (num_lt + num_gt == r - l + 1) {
    assert(pos_X < l || pos_X > r);
    assign_block(lt, l, r, num_lt, 1, 0);
    assign_block(gt, l, r, num_lt, 0, 1);
  } else {
    assert(l <= pos_X && pos_X <= r);
    pos_X = l + num_lt;
    assign_block(lt, l, r, num_lt, 1, 0);
    assign_block(gt, l, r, num_lt+1, 0, 1);
  }
}

void sort_descending(int l, int r) {
  int num_lt = lt->rangeSum(l, r);
  int num_gt = gt->rangeSum(l, r);

  if (num_lt + num_gt == r - l + 1) {
    assert(pos_X < l || pos_X > r);
    assign_block(lt, l, r, num_gt, 0, 1);
    assign_block(gt, l, r, num_gt, 1, 0);
  } else {
    assert(l <= pos_X && pos_X <= r);
    pos_X = l + num_gt;
    assign_block(lt, l, r, num_gt+1, 0, 1);
    assign_block(gt, l, r, num_gt, 1, 0);
  }
}

void check() {
  for (int i=0; i<N; i++) {
    int x = lt->rangeSum(i, i);
    int y = (pos_X == i ? 1 : 0);
    int z = gt->rangeSum(i, i);

    assert(x + y + z == 1);
    assert(0 <= x && x <= 1);
    assert(0 <= y && x <= 1);
    assert(0 <= z && x <= 1);

    // if (x == 1) cout << "< ";
    // if (y == 1) cout << "X ";
    // if (z == 1) cout << "> ";
  }
  // cout << endl;
}

i32 main() {

  cin >> N >> Q >> X;

  auto _lt = vector<int>(N, 0);
  auto _gt = vector<int>(N, 0);

  for (int i=0; i<N; i++) {
    int p;
    cin >> p;
    if (p < X) {
      _lt[i] = 1;
    } else if (p > X) {
      _gt[i] = 1;
    } else {
      pos_X = i;
    }
  }

  lt = new SegTreeAssignSum(_lt);
  gt = new SegTreeAssignSum(_gt);

  // dump();
  while (Q --> 0) {
    int c, l, r;
    cin >> c >> l >> r;
    l--; r--;

    // cout << "proc" << c << l << r << endl;

    if (c == 1) {
      sort_ascending(l, r);
    } else if (c == 2) {
      sort_descending(l, r);
    } else {
      assert(false);
    }
    // check();
  }

  cout << (pos_X+1) << endl;

  return 0;
}
