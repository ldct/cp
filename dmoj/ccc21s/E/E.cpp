#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

int M,N;
map<int, int> counter;
vector<pair<int, int>> events;
vector<tuple<int, int, int>> constraints;

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
struct Gcd { long long operator()(long long x, long long y) const { return gcd(x, y); } };

int calc() {
  int ret = 1;
  for (int i=1; i<=16; i++) {
    if (counter[i] > 0) ret = lcm(ret, i);
  }
  return ret;
}

int main() {

  for (int i=1; i<=16; i++) counter[i] = 0;

  cin >> N >> M;
  for (int i=0; i<M; i++) {
    int x, y, z;
    cin >> x >> y >> z;
    x--; y--;
    constraints.push_back({x, y, z});
    events.push_back({x, +z});
    events.push_back({y+1, -z});
  }
  sort(events.begin(), events.end());

  vector<long long> ret;

  int j=0;
  for (int i=0; i<N; i++) {
    while (j < events.size() && events[j].first == i) {
      int z = events[j].second;
      if (z > 0) {
        counter[z]++;
      } else {
        counter[-z]--;
      }
      j += 1;
    }
    ret.push_back(calc());
  }

  auto t = SegTree<Gcd, 0>(ret);

  for (const auto c : constraints) {
    if (get<2>(c) != t.rangeSum(get<0>(c), get<1>(c))) {
      cout << "Impossible" << endl; return 0;
    }
  }

  for (int i=0; i<ret.size(); i++) {
    cout << ret[i];
    if (i != ret.size()-1) cout << " ";
  }
  cout << endl;

  return 0;
}
