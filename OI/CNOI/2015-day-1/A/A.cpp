#include <bits/stdc++.h>
using namespace std;

int T;

// tag:disjoint set union
// tag:DSU
// tag:union-find
struct UF {
	vector<int> e;
	UF(int n) : e(n, -1) {}
	bool sameSet(int a, int b) { return find(a) == find(b); }
	int size(int x) { return -e[find(x)]; }
	int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
	bool join(int a, int b) {
		a = find(a), b = find(b);
		if (a == b) return false;
		if (e[a] > e[b]) swap(a, b);
		e[a] += e[b]; e[b] = a;
		return true;
	}
};

template<class T> void sort_unique(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()),v.end());}

string ans(vector<pair<int, int>>& sep, vector<pair<int, int>>& same, vector<int>& indices) {
  sort_unique(indices);
  unordered_map<int, int> comp;

  for (int i=0; i<indices.size(); i++) {
    comp[indices[i]] = i;
  }

  UF uf(indices.size());

  for (const auto& [i, j] : same) {
    uf.join(comp[i], comp[j]);
  }

  for (const auto& [i, j] : sep) {
    if (uf.sameSet(comp[i], comp[j])) return "NO";
  }
  return "YES";
}

int main() {

  cin >> T;
  while (T --> 0) {

    vector<int> indices;
    vector<pair<int, int>> same;
    vector<pair<int, int>> sep;

    int N;
    cin >> N;
    for (int n=0; n<N; n++) {
      int i, j, e;
      cin >> i >> j >> e;
      i--; j--;

      indices.push_back(i);
      indices.push_back(j);

      if (e == 1) {
        same.push_back({i, j});
      } else {
        sep.push_back({i, j});
      }
    }
    cout << ans(sep, same, indices) << endl;
  }

  return 0;
}
