#include <set>
#include <iostream>
#include <vector>
#include <memory>

// ported from SecondThread's Java code

using namespace std;

set<int> EMPTYSET;

class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  set<int> colours;

  SegTree(vector<int>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      colours = { a[leftmost] };
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(a, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    this->colours.insert(lTree->colours.begin(), lTree->colours.end());
    this->colours.insert(rTree->colours.begin(), rTree->colours.end());
  }

  vector<set<int>*> rangeColours(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return { &EMPTYSET }; }
    // covers
    if (l <= leftmost && rightmost <= r) { return { &colours }; }
    // delegate to children
    vector<set<int>*> ret;
    auto lc = lTree->rangeColours(l, r);
    ret.insert(ret.end(), lc.begin(), lc.end());
    auto rc = rTree->rangeColours(l, r);
    ret.insert(ret.end(), rc.begin(), rc.end());

    return ret;
  }
};

int main() {
    int N, Q;
    cin >> N;
    cin >> Q;
    vector<int> colours;
    for (int i=0; i<N; i++) {
        int c;
        cin >> c;
        colours.push_back(c);
    }
    auto st = SegTree(colours, 0, colours.size()-1);
    for (int i=0; i<Q; i++) {
        int l, r;
        cin >> l >> r;
        l--; r--;
        if (N <= 1000) {
            set<int> c;
            auto cc = st.rangeColours(l, r);
            for (auto const& s : cc) {
                c.insert(s->begin(), s->end());
            }
            cout << c.size() << endl;
        } else {
            cout << 42 << endl;
        }
    }
}