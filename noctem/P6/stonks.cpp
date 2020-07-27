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
  int sum;


  SegTree(vector<int>&a, int _leftmost, int _rightmost) {
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

  void pointIncrement(int idx, int newVal) {
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

  int rangeSum(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return sum; }
    // delegate to children
    return lTree->rangeSum(l, r) + rTree->rangeSum(l, r);
  }
};


int N;

int main() {

  ifstream inFile;
  inFile.open("stonks.in");
  assert(inFile);

  ofstream outFile;
  outFile.open("stonks.out");
  assert(outFile);

  inFile >> N;

  vector<pair<int, int>> p;

  for (int i=0; i<N; i++) {
    int pi;
    inFile >> pi;
    p.push_back(make_pair(pi, i));
  }

  sort(p.begin(), p.end());

  auto p2 = p;
  auto old_p = p;

  for (int i=0; i<p2.size(); i++) {
    p2[i].first = p2[i].second;
    p2[i].second = i;
  }

  sort(p2.begin(), p2.end());

  vector<int> indices;

  for (int i=0; i<p2.size(); i++) {
    indices.push_back(p2[i].second);
  }

  // cout << "p=" << p << endl;

  // cout << "indices=" << indices << endl;
    
  vector<int> arr;
  for (int i=0; i<indices.size(); i++) {
    arr.push_back(1);
  }

  auto st = SegTree(arr, 0, arr.size()-1);

  int bestday = -1;
  int bestrun = 0;

  for (const auto i : indices) {
    st.pointIncrement(i,-1);

    int sum = st.rangeSum(i, N-1);

    if (sum > bestrun) {
      bestday = old_p[i].second + 1;
      bestrun = sum;
    }
  }

  assert(bestday != -1);

  outFile << bestday << endl;

  return 0;
}
