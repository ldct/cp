#include <bits/stdc++.h>

// ported from SecondThread's Java code

using namespace std;

class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  long long sum;
  long long prefix;
  long long suffix;
  long long max_ssum;


  SegTree(vector<long long>&a, int _leftmost, int _rightmost) {
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      sum = a[leftmost];
      prefix = max(0LL, sum);
      suffix = max(0LL, sum);
      max_ssum = max(0LL, sum);
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
    this->prefix = max(lTree->prefix, lTree->sum + rTree->prefix);
    this->suffix = max(rTree->suffix, lTree->suffix + rTree->sum);
    this->max_ssum = max({lTree->max_ssum, rTree->max_ssum, lTree->suffix + rTree->prefix});
  }

  void pointSet(int idx, int newVal) {
    if (leftmost == rightmost && leftmost == idx) {
      sum = newVal;
      prefix = max(0LL, sum);
      suffix = max(0LL, sum);
      max_ssum = max(0LL, sum);
    } else {
      if (idx <= lTree->rightmost) {
        lTree->pointSet(idx, newVal);
      } else {
        rTree->pointSet(idx, newVal);
      }
      recalc();
    }
  }
};

int main() { 
  int N, M;
  cin >> N >> M;
  vector<long long>A(N, 0);
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A[i] = a;
  }
  auto s = SegTree(A, 0, A.size()-1);
  cout << s.max_ssum << endl;
  for (int j=0; j<M; j++) {
    int i,v;
    cin >> i >> v;
    s.pointSet(i, v);
    cout << s.max_ssum << endl;
  }

  return 0;
}
