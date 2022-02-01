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

// segment tree for range sum
class SegTreeSum {
public:
  unique_ptr<SegTreeSum> lTree;
  unique_ptr<SegTreeSum> rTree;
  int leftmost;
  int rightmost;
  long long sum;

  SegTreeSum(vector<long long>& a) : SegTreeSum(a, 0, a.size()-1) {}

  SegTreeSum(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      sum = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTreeSum>(new SegTreeSum(a, leftmost, mid));
      rTree = unique_ptr<SegTreeSum>(new SegTreeSum(a, mid+1, rightmost));

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

  long long rangeSum(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return sum; }
    // delegate to children
    return lTree->rangeSum(l, r) + rTree->rangeSum(l, r);
  }
};

int N, Q;
int colour[500009];
vector<pair<pair<int, int>, pair<int, int>>> queries;
int repr[500009];

i32 main() {

  memset(repr, -1, sizeof(repr));

  cin >> N >> Q;
  for (int i=0; i<N; i++) cin >> colour[i];

  for (int i=0; i<Q; i++) {
    int l, r;
    cin >> l >> r;
    l--; r--;
    queries.push_back({{r, l}, {i, -1}});
  }

  sort(queries.begin(), queries.end());

  // cout << queries << endl;

  auto backing = vector<int>(N, 0);
  auto st = SegTreeSum(backing);

  int next_r = 0;
  for (int j=0; j<queries.size(); j++) {
    auto q = queries[j];
    int r = q.first.first;
    int l = q.first.second;

    int qid = q.second.first;

    while (next_r <= r) {
      int c = colour[next_r];
      if (repr[c] != -1) {
        st.pointSet(repr[c], 0);
      }
      repr[c] = next_r;
      st.pointSet(repr[c], 1);
      // cout << "set representative for " << c << endl;
      next_r++;
    }
    // cout << "answer query " << qid << " " << st.rangeSum(l, r) << endl;
    queries[j] = make_pair(
      make_pair(qid, st.rangeSum(l, r)),
      make_pair(-1, -1)
    );
  }

  sort(queries.begin(), queries.end());

  for (auto q : queries) {
    cout << q.first.second << endl;
  }

  return 0;
}
