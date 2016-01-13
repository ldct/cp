#include <iostream>
#include <vector>
#include <map>

using namespace std;

int N, M;

map<int, vector<int> > neighbours;
map<int, int> size;
map<int, long long> memoMaxDecreasing;

long long maxDecreasing(int n) {
	// maximum length of decreasing sequence starting at n

	if (memoMaxDecreasing.find(n) != memoMaxDecreasing.end()) {
		return memoMaxDecreasing[n];
	}

	long long ret = 1;

	vector<int> myNeighbours = neighbours[n];
	for (int i=0; i<size[n]; i++) {
		if (myNeighbours[i] > n) continue;
		ret = max(ret, 1 + maxDecreasing(myNeighbours[i]));
	}

	memoMaxDecreasing[n] = ret;
	return ret;
}

int main () {
	cin >> N >> M;

	for (int n=0; n<N; n++) {
		neighbours[n] = vector<int>();
	}

	for (int m=0; m<M; m++) {
		int u, v;
		cin >> u >> v;
		neighbours[u].push_back(v);
		neighbours[v].push_back(u);
	}

	for (int n=1; n<=N; n++) {
		size[n] = neighbours[n].size();
	}

	long long maxScore = 0;

	for (int n=1; n<=N; n++) {
		maxScore = max(maxScore, size[n] * maxDecreasing(n));
	}

	cout << maxScore << endl;

}