#include <iostream>
#include <vector>
#include <set>

using namespace std;

int N;
set<long long> s;
vector<int> ans;

int main () {
	cin >> N;

	for (int i=1; i<=N; i++) {
		int p;
		cin >> p;
		if (s.find(p) != s.end()) {
			ans.push_back(i);
			s = set<long long>();
		} else {
			s.insert(p);
		}
	}

	if (ans.size() == 0) {
		cout << -1 << endl;
		return 0;
	} else {
		cout << ans.size() << endl;
		ans[ans.size()-1] = N;
		cout << "1 " << ans[0] << endl;
		for (int i=1; i<ans.size(); i++) {
			cout << ans[i-1]+1 << " " << ans[i] << endl;
		}
	}
}