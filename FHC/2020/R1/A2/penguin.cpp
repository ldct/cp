#include <bits/stdc++.h>
using namespace std;

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

int n, Q;
ll a[500000];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> n >> Q;
	lazy_seg_tree t(n);
	for (int i=0; i<n; ++i)
		cin >> a[i];
	t.build(a);

	for (int qNum=0; qNum<Q; ++qNum) {
		int type, l, r; cin >> type >> l >> r, --r;
		if (type==0) {
			ar<ll, 2> val;
			cin >> val[0] >> val[1];
			t.upd(l, r, val);
		}
		if (type==1) {
			cout << t.qry(l, r) << '\n';
		}
	}
	return 0;
}