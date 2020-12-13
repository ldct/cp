class MinTree {
public:
  unique_ptr<MinTree> lTree;
  unique_ptr<MinTree> rTree;
  int leftmost;
  int rightmost;
  long long _min;

  MinTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      this->_min = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<MinTree>(new MinTree(a, leftmost, mid));
      rTree = unique_ptr<MinTree>(new MinTree(a, mid+1, rightmost));

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

class MaxTree {
public:
  unique_ptr<MaxTree> lTree;
  unique_ptr<MaxTree> rTree;
  int leftmost;
  int rightmost;
  long long _max;

  MaxTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      this->_max = a[leftmost];
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<MaxTree>(new MaxTree(a, leftmost, mid));
      rTree = unique_ptr<MaxTree>(new MaxTree(a, mid+1, rightmost));

      recalc();
    }
  }
  void recalc() {
    if (leftmost == rightmost) return;
    this->_max = max(lTree->_max, rTree->_max);
  }

  void pointSet(int idx, int newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      _max = newVal;
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }

  long long rangeMax() { return _max; }
  long long rangeMax(int l, int r) {
    // entirely disjoint
    if (rightmost < l || r < leftmost) { return LLONG_MIN; }
    // covers
    if (l <= leftmost && rightmost <= r) { return this->_max; }
    // delegate to children
    return max(lTree->rangeMax(l, r), rTree->rangeMax(l, r));
  }
};