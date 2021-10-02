#include <bits/stdc++.h>
using namespace std;

constexpr int MODULUS = 998244353;

long long modexp(long long b, long long e) {
	long long ans = 1;
	for (; e; b = b * b % MODULUS, e /= 2)
		if (e & 1) ans = ans * b % MODULUS;
	return ans;
}

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
  long long sum;

  SegTree(vector<long long>& a) : SegTree(a, 0, a.size()-1) {}

  SegTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      sum = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(a, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(a, mid+1, rightmost));

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

  long long rangeSum(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return sum; }
    // delegate to children
    return lTree->rangeSum(l, r) + rTree->rangeSum(l, r);
  }
};

int N;
vector<int> A;

int main() {

  vector<long long> E;

  cin >> N;
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A.push_back(a);
    E.push_back(0);
  }

  vector<pair<int, int>> pairs(N);
  for(int i = 0; i < N; ++i) {
    pairs[i] = {A[i], i};
  }
  sort(pairs.begin(), pairs.end());
  int nxt = 0;
  for(int i = 0; i < N; ++i) {
    if(i > 0 && pairs[i-1].first != pairs[i].first) nxt++;
    A[pairs[i].second] = nxt;
  }

  // cout << A << endl;

  auto s = SegTree(E);
  long long ret = 0;
  for (int i=N-1; i!=-1; i--) {
    if (i != N-1) {
      long long c = s.rangeSum(A[i], N);
      c %= MODULUS;
      c *= modexp(2, MODULUS-2-i);
      c %= MODULUS;
      ret += c;
      ret %= MODULUS;
    }
    s.pointIncrement(A[i], modexp(2, i));
  }

  cout << ret << endl;

  return 0;
}
