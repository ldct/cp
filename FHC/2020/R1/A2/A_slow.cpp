#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

constexpr int MODULUS = 1000000007;

// START


#define ll long long
#define ar array

ar<ll, 2>& operator+=(ar<ll, 2> &a, const ar<ll, 2> &b) {
	a[0]=(a[0]*b[0]);
	a[1]=(a[1]*b[0]+b[1]);
	return a;
}

struct lazy_seg_tree { /*penguinhacker*/
	int n;
	const ar<ll, 2> ID={1, 0};
	vector<ll> seg;
	vector<ar<ll, 2>> lazy;
	lazy_seg_tree(int _n) : n(_n) {
		seg.assign(4*n, 0);
		lazy.assign(4*n, ID);
	}

	void build(int u, int l, int r, ll *v) {
		if (l==r) { seg[u]=v[l]; return; }
		int mid=(l+r)/2; build(2*u, l, mid, v), build(2*u+1, mid+1, r, v);
		pull(u);
	}
	void build(ll *v) {build(1, 0, n-1, v);}

	void push(int u, int l, int r) {
		seg[u]=(seg[u]*lazy[u][0]+(r-l+1)*lazy[u][1]);
		if (l!=r) lazy[2*u]+=lazy[u], lazy[2*u+1]+=lazy[u];
		lazy[u]=ID;
	}
	void pull(int u) { seg[u]=seg[2*u]+seg[2*u+1]; }

	void upd(int x, int y, ar<ll, 2> val, int u, int l, int r) {
		push(u, l, r); if (l>y||r<x) return;
		if (x<=l&&r<=y) { lazy[u]+=val; push(u, l, r); return; }
		int mid=(l+r)/2; upd(x, y, val, 2*u, l, mid), upd(x, y, val, 2*u+1, mid+1, r);
		pull(u);
	}
	void upd(int x, int y, ar<ll, 2> val) {upd(x, y, val, 1, 0, n-1);}

	int qry(int x, int y, int u, int l, int r) {
		push(u, l, r); if (l>y||r<x) return 0;
		if (x<=l&&r<=y) return seg[u];
		int mid=(l+r)/2;
		int k=qry(x, y, 2*u, l, mid)+qry(x, y, 2*u+1, mid+1, r);
		return k;
	}
	int qry(int x, int y) {return qry(x, y, 1, 0, n-1);}

    int rangeSum(int l, int r) { return qry(l, r); }
    void rangeSet(int l, int r, long long v) {
        upd(l, r, {0, v});
    }
};
// END

class FakeTree {
public:
  vector<long long> elems;
  FakeTree(vector<long long>& A) {
    for (int i=0; i<A.size(); i++) {
      elems.push_back(A[i]);
    }
  }
  void rangeSet(int l, int r, long long v) {
    for (int i=l; i<=r; i++) {
      elems[i] = v;
    }
  }
  long long rangeSum(int l, int r) {
    long long ret = 0;
    for (int i=l; i<=r; i++) {
      ret += elems[i];
      ret %= MODULUS;
    }
    return ret;
  }
};

int N;
int K;

vector<long long> L;
vector<long long> W;
vector<long long> H;

vector<long long> coordinates; 
unordered_map<long long, int> short_x;

long long ans() {
  coordinates.clear();
  short_x.clear();
  for (int i=0; i<L.size(); i++) {
    coordinates.push_back(L[i]);
    coordinates.push_back(L[i] + W[i]);
    coordinates.push_back(L[i] + 1);
    coordinates.push_back(L[i] - 1);
    coordinates.push_back(L[i] + W[i] + 1);
    coordinates.push_back(L[i] + W[i] - 1);
  }

  sort(coordinates.begin(), coordinates.end());
  coordinates.erase(unique(coordinates.begin(), coordinates.end()), coordinates.end());


  for (int i=0; i<coordinates.size(); i++) {
    short_x[coordinates[i]] = i;
  }

  vector<long long> v_number_line;
  for (int i=0; i<coordinates.size() - 1 ; i++) {
    v_number_line.push_back(coordinates[i+1] - coordinates[i]);
  }

  // auto unoccupied = lazy_seg_tree(v_number_line.size());
  // unoccupied.build(&v_number_line[0]);

  // auto unoccupied_fat = lazy_seg_tree(v_number_line.size());
  // unoccupied_fat.build(&v_number_line[0]);

  auto unoccupied = FakeTree(v_number_line);
  auto unoccupied_fat = FakeTree(v_number_line);

  vector<long long> _heights;
  for (int i=0; i<coordinates.size(); i++) {
    _heights.push_back(0);
  }

  // auto l_heights = lazy_seg_tree(_heights.size());
  // l_heights.build(&_heights[0]);

  // auto r_heights = lazy_seg_tree(_heights.size());
  // r_heights.build(&_heights[0]);

  auto l_heights = FakeTree(_heights);
  auto r_heights = FakeTree(_heights);

  vector<long long> Px, Py;

  long long curr_x = 0;
  long long curr_y = 0;

  for (int i=0; i<L.size(); i++) {

    // cout << "i=" << i << endl;
    
    int l = short_x[L[i]];
    int r = short_x[L[i] + W[i]];

    int lll = short_x[L[i] + 1];
    int rrr = short_x[L[i] + W[i] - 1];

    bool set_l = false;
    bool set_r = false;

    if (unoccupied_fat.rangeSum(l, l) > 0) {
      curr_y += H[i];
      set_l = true;
    }

    if (unoccupied_fat.rangeSum(r, r) > 0) {
      curr_y += H[i];
      set_r = true;
    }
    curr_y %= MODULUS;

    int crossed_heights = 0;
    if (l_heights.rangeSum(lll, r)) crossed_heights += l_heights.rangeSum(lll, r);
    if (r_heights.rangeSum(l, rrr)) crossed_heights += r_heights.rangeSum(l, rrr);

    
    l_heights.rangeSet(lll, r, 0);
    r_heights.rangeSet(l, rrr, 0);
    curr_y -= (H[i]*crossed_heights);
    curr_y = (curr_y % MODULUS + MODULUS) % MODULUS;
  
    curr_x += unoccupied.rangeSum(l, r-1);
    curr_x %= MODULUS;
    unoccupied.rangeSet(l, r-1, 0);
    unoccupied_fat.rangeSet(l, r, 0);

    Px.push_back(curr_x);
    Py.push_back(curr_y);

    if (set_l) {
      // cout << "set " << L[i] << " " << l << endl;
      l_heights.rangeSet(l, l, 1);
    }
    if (set_r) {
      // cout << "set " << L[i] + W[i] << endl;
      r_heights.rangeSet(r, r, 1);
    }
  }

  vector<long long> P;

  for (int i=0; i<L.size(); i++) {
    P.push_back(2*Px[i] + Py[i]);
  }


  // cout << P << endl;

  long long ret = 1;
  for (const auto p : P) {
    ret *= p;
    ret %= MODULUS;
  }

  return ret;
}

int main() {
  
  int T;
  cin >> T;
  
  for (int t=1; t <= T; t++) {

    cin >> N >> K;

    L.clear();
    for (int k=0; k<K; k++) {
      long long l;
      cin >> l;
      L.push_back(l);
    }

    long long a,b,c,d;
    cin >> a >> b >> c >> d;

    while (L.size() < N) {
      L.push_back((a*L[L.size()-2] + b*L[L.size()-1] + c) % d + 1);
    }

    W.clear();
    for (int k=0; k<K; k++) {
      long long w;
      cin >> w;
      W.push_back(w);
    }

    cin >> a >> b >> c >> d;

    while (W.size() < N) {
      W.push_back((a*W[W.size()-2] + b*W[W.size()-1] + c) % d + 1);
    }

    H.clear();
    for (int k=0; k<K; k++) {
      long long h;
      cin >> h;
      H.push_back(h);
    }

    cin >> a >> b >> c >> d;

    while (H.size() < N) {
      H.push_back((a*H[H.size()-2] + b*H[H.size()-1] + c) % d + 1);
    }

    cout << "Case #" << t << ": " << ans() << endl;
  }
    
  return 0;
}
