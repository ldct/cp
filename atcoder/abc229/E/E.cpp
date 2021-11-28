#include <bits/stdc++.h>
using namespace std;

struct UF {
	vector<int> e;
    int cc = 0;
    unordered_set<int> activated;
    vector<int> neighbours[200009];

	UF(int n) : e(n, -1) {}

    void add_edge(int u, int v) {
        neighbours[u].push_back(v);
        neighbours[v].push_back(u);
    }
    void activate(int u) {
        activated.insert(u);
        cc++;
        for (auto v : neighbours [u]) {
            if (activated.count(v)) {
                // cout << "joining " << u << " " << v << endl;
                join(u, v);
            }
        }
    }
	bool sameSet(int a, int b) { return find(a) == find(b); }
	int size(int x) { return -e[find(x)]; }
	int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
	bool join(int a, int b) {
		a = find(a), b = find(b);
		if (a == b) return false;
        cc--;
		if (e[a] > e[b]) swap(a, b);
		e[a] += e[b]; e[b] = a;
		return true;
	}
};

int main() {

    int N, M;
    cin >> N >> M;
    UF uf(N+1);
    for (int i=0; i<M; i++) {
        int u, v;
        cin >> u >> v;
        uf.add_edge(u, v);
    }

    vector<int> ret;
    for (int u = N; u!=1; u--) {
        uf.activate(u);
        ret.push_back(uf.cc);
        // cout << "activated " << u << endl;
    }

    reverse(ret.begin(), ret.end());
    ret.push_back(0);
    for (auto r : ret) cout << r << endl;
    return 0;
}
