#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

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

constexpr int MAX_N = 200009;
int N;
long long A[MAX_N];
vector<vi> children;
vector<vi> parents;
long long paths_ending[MAX_N];
long long paths_starting[MAX_N];
vector<pii> edges;

int main() {
  cin >> N;
  children = vector<vi>(N);
  parents = vector<vi>(N);
  for (int i=0; i<N; i++) {
    cin >> A[i];
  }
  for (int i=0; i<N-1; i++) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    children[u].push_back(v);
    parents[v].push_back(u);
    edges.push_back({u, v});
  }

  auto t = topoSort(children);

  for (int i=0; i<N; i++) paths_ending[i] = 0;
  for (int i=0; i<N; i++) paths_starting[i] = 0;

  for (auto u : t) {
    for (auto child : children[u]) {
      paths_ending[child] += paths_ending[u] + A[u];
    }
  }

  reverse(t.begin(), t.end());
  for (auto u : t) {
    for (auto parent : parents[u]) {
      paths_starting[parent] += paths_starting[u] + A[u];
    }
  }

  long long tv = 0;

  for (int i=0; i<N; i++) {
    tv += paths_ending[i]*A[i];
  }

  for (int i=0; i<N; i++) {
    tv += A[i]*(A[i]-1);
  }

  long long ma = 0;

  for (auto e : edges) {
    int u = e.first;
    int v = e.second;

    long long additional = (A[v] + paths_ending[v] - (paths_ending[u] + A[u])) * (A[u] + paths_starting[u] - (paths_starting[v] + A[v]));
    ma = max(ma, additional);
  }

  cout << tv + ma << endl;

  return 0;
}
