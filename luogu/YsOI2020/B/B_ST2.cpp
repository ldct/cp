#include <bits/stdc++.h>

using namespace std;

template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }

template<class T1, class T2>
ostream& operator << (ostream& os, const pair<T1,T2>& v) {
    return os << "(" << v.first << ", " << v.second << ")";
}

constexpr int MODULUS = 998244353;

long long modpow(long long b, long long e) {
	long long ans = 1;
	for (; e; b = b * b % MODULUS, e /= 2)
		if (e & 1) ans = ans * b % MODULUS;
	return ans;
}

vector<long long> A;

class SegTree {
public:
  unique_ptr<SegTree> lTree;
  unique_ptr<SegTree> rTree;
  int leftmost;
  int rightmost;
  long long a;
  long long r;
  int f;

  SegTree(vector<long long>&arr, int _leftmost, int _rightmost) {
    a = 1;
    r = 1;
    leftmost = _leftmost;
    rightmost = _rightmost;
    if (leftmost == rightmost) {
      return;
    } else {
      int mid = (leftmost + rightmost) / 2;

      lTree = unique_ptr<SegTree>(new SegTree(arr, leftmost, mid));
      rTree = unique_ptr<SegTree>(new SegTree(arr, mid+1, rightmost));
    }
  }
  vector<pair<int,pair<long long,long long>>> pg(int idx) {
    if (leftmost == rightmost && leftmost == idx) {
      return { make_pair(f, make_pair(a, r))};
    } else {
      vector<pair<int,pair<long long,long long>>> v;
      if (idx <= lTree->rightmost) {
        v = lTree->pg(idx);
      } else {
        v = rTree->pg(idx);
      }
      v.push_back(make_pair(f, make_pair(a, r)));
      return v;
    }
  }
  long long pointGet(int idx) {
    auto v = pg(idx);
    sort(v.begin(), v.end());

    cout << "pg=" << v << endl;

    auto ret = A[idx];

    for (const auto& e : v) {
      auto [f, ar] = e;
      auto [a, r] = ar;
      ret = ((long long)a*modpow(ret, r)) % MODULUS;
    }

    return ret;
  }
  void rangeMP(int ll, int rr, long long m, long long p, int f) {
    // cout << "rangeMP " << leftmost << " " << rightmost << " " << m << " " << p << endl;
    // entirely disjoint
    if (rightmost < ll || rr < leftmost) { return; }
    // covers
    if (ll <= leftmost && rightmost <= rr) { 
      // cout << "rangeMP covers " << leftmost << " " << rightmost << " " << m << " " << p << endl;
      // cout << "r=" << r << "a=" << a << endl;
      r = (r*p) % (MODULUS-1);
      a = (m*modpow(a,p)) % MODULUS;
      // cout << "r=" << this->r << "a=" << this->a << endl;
      this->f = f;
      return; 
    }
    // delegate to children
    lTree->rangeMP(ll, rr, m, p, f);
    rTree->rangeMP(ll, rr, m, p, f);
  }
};

SegTree* ST;

int N, M;

void query_one(int l, int r, long long x, int f) {
  ST->rangeMP(l, r, 1, x, f);
}

void query_two(int l, int r, int y, int f) {
  long long mul_by = ST->pointGet(y);
  cout << "mul_by=" << mul_by << endl;
  ST->rangeMP(l, r, mul_by, 1, f);
}

void query_three(int z) {
  cout << ST->pointGet(z) << endl;
}

int main() {
  
  cin >> N >> M;

  for (int i=0; i<N; i++) {
    long long a;
    cin >> a;
    A.push_back(a);
  }

  ST = new SegTree(A, 0, A.size()-1);

  for (int i=0; i<M; i++) {
    int query_type;
    cin >> query_type;

    if (query_type == 1) {
      long long l, r, x;
      cin >> l >> r >> x;
      query_one(l-1, r-1, x, i+1);
    } else if (query_type == 2) {
      long long l, r, y;
      cin >> l >> r >> y;
      query_two(l-1, r-1, y-1, i+1);
    } else if (query_type == 3) {
      int z;
      cin >> z;
      query_three(z-1);
    }
    // cout << "A=" << A << endl;
  }

  return 0;
}
