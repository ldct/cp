class FreqTree {
public:
  unique_ptr<FreqTree> lTree;
  unique_ptr<FreqTree> rTree;
  int leftmost;
  int rightmost;
  map<int, int> freq;

  FreqTree(vector<int>& a) : FreqTree(a, 0, a.size()-1) {}

  FreqTree(vector<int>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      freq[a[leftmost]] = 1;
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<FreqTree>(new FreqTree(a, leftmost, mid));
      rTree = unique_ptr<FreqTree>(new FreqTree(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    for (auto k : lTree->freq) freq[k.first] += k.second;
    for (auto k : rTree->freq) freq[k.first] += k.second;
  }

  int query(int l, int r, int k) {
    if (l > r) return 0;
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return 0; }
    // covers
    if (l <= leftmost && rightmost <= r) { return freq[k]; }
    // delegate to children
    return lTree->query(l, r, k) + rTree->query(l, r, k);
  }
};