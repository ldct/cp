#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

vi topoSort(const vector<vi>& gr) {
	vi indeg(sz(gr)), ret;
	for (auto& li : gr) for (int x : li) indeg[x]++;
	queue<int> q; // use priority queue for lexic. smallest ans.
	rep(i,0,sz(gr)) if (indeg[i] == 0) q.push(-i);
	while (!q.empty()) {
		int i = -q.front(); // top() for priority queue
		ret.push_back(i);
		q.pop();
		for (int x : gr[i])
			if (--indeg[x] == 0) q.push(-x);
	}
	return ret;
}

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << (char)(v[i]+'a'); if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

int N, K;

char words[1000009][109];

int matrix[26][26];
vector<vi> neighbours(26);

bool bad;

void populate(int offset, int start, int end) {
    int last = start;
    if (offset >= 100) return;

    for (int i=start; i<=end; i++) {
        if (words[i][offset] != words[last][offset]) {
            if (words[i][offset] == '_') {
                bad = true;
            } else if (words[last][offset] == '_') {
                // pass
            } else {
                int u = words[last][offset] - 'a';
                int v = words[i][offset] - 'a';

                if (matrix[v][u] == 1) {
                    bad = true;
                } else {
                    if (matrix[u][v] == 1) {
                        // pass
                    } else {
                        matrix[u][v] = 1;
                        neighbours[u].push_back(v);
                    }
                }
            }
            populate(offset+1, last, i-1);
            last = i;
        }
    }
    populate(offset+1, last, end);
}

bool present[26];

int main() {
    scanf("%d %d\n", &N, &K);

    for (int i=0; i<26; i++) present[i] = false;

    for (int i=0; i<N; i++) {

        int idx;
        scanf("%d\n", &idx);

        for (int j=0; j<K; j++) {
            int si = K*idx + j;
            scanf("%s\n", words[si]);
            // printf("[%d] read %d bytes %s\n", si, strlen(words[si]), words[si]);
            for (int t=0; t<strlen(words[si]); t++) {
                char c = words[si][t];
                present[c - 'a'] = true;
            }
            int k;
            for (k=strlen(words[si]); k < 100; k++) { // XXX replace
                words[si][k] = '_';
            }
            words[si][k] = 0;
        }
    }

    // printf("read liao\n");
    // return 0;

    // for (int i=0; i<N*K; i++) { printf("words[%d] = %s\n", i, words[i]); }

    bad = false;

    for (int u=0;u<26;u++) for (int v=0;v<26;v++) matrix[u][v] = 0;

    populate(0, 0, N*K-1);

    if (bad) {
        cout << "IMPOSSIBLE" << endl;
        return 0;
    }

    auto ts = topoSort(neighbours);

    if (ts.size() != 26) {
        cout << "IMPOSSIBLE" << endl;
        return 0;
    }

    for (const auto& c : ts) {
        if (present[c]) {
            cout << (char)(c + 'a');
        }
    }

    cout << endl;
}