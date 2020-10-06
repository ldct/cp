#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

bool dfs(int a, int L, vector<vi>& g, vi& btoa, vi& A, vi& B) {
	if (A[a] != L) return 0;
	A[a] = -1;
	for (int b : g[a]) if (B[b] == L + 1) {
		B[b] = 0;
		if (btoa[b] == -1 || dfs(btoa[b], L + 1, g, btoa, A, B))
			return btoa[b] = a, 1;
	}
	return 0;
}

int hopcroftKarp(vector<vi>& g, vi& btoa) {
	int res = 0;
	vi A(g.size()), B(btoa.size()), cur, next;
	for (;;) {
		fill(all(A), 0);
		fill(all(B), 0);
		/// Find the starting nodes for BFS (i.e. layer 0).
		cur.clear();
		for (int a : btoa) if(a != -1) A[a] = -1;
		rep(a,0,sz(g)) if(A[a] == 0) cur.push_back(a);
		/// Find all layers using bfs.
		for (int lay = 1;; lay++) {
			bool islast = 0;
			next.clear();
			for (int a : cur) for (int b : g[a]) {
				if (btoa[b] == -1) {
					B[b] = lay;
					islast = 1;
				}
				else if (btoa[b] != a && !B[b]) {
					B[b] = lay;
					next.push_back(btoa[b]);
				}
			}
			if (islast) break;
			if (next.empty()) return res;
			for (int a : next) A[a] = lay;
			cur.swap(next);
		}
		/// Use DFS to scan for augmenting paths.
		rep(a,0,sz(g))
			res += dfs(a, 0, g, btoa, A, B);
	}
}

int N, M;

constexpr int MAX_N = 10009;

map<int, int> weights[MAX_N];

vector<vi> neighbours(N);
vector<int> btoa;

int match_size(int d) {

    neighbours = vector<vi>(N);

    btoa.clear(); for (int i=0; i<N; i++) { btoa.push_back(-1); }

    for (int i=0;i<N;i++) {
        for (const auto& [k, v] : weights[i]) {
            if (v <= d) {
                neighbours[i].push_back(k);
            }
        }
    }

    return hopcroftKarp(neighbours, btoa);
}

bool ok(int d) {
    return match_size(d) == N;
}

int main() {
    cin >> N >> M;

    for (int i=0; i<M; i++) {
        int u,v,d;
        cin >> u >> v >> d;
        u--; v--;

        weights[u][v] = d;
    }

    int low = 0;
    int high = 1000000009;

    if (ok(low)) {
        cout << "wtf is this" << endl;
        return 0;
    }

    if (!ok(high)) {
        cout << -1 << endl;
        return 0;
    }

    for (int i=0; i<32; i++) {
        int mid = (low + high) / 2;
        if (ok(mid)) {
            high = mid;
        } else {
            low = mid;
        }
    }

    for (int i=low; i<1000000009; i++) {
        if (ok(i)) {
            cout << i << endl;
            return 0;
        }
    }

}