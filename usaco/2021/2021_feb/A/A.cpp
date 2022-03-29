#include <bits/stdc++.h>
using namespace std;
 
int main() {
	int N; cin >> N;
	vector<int> A(N); 
	int mx = 0;
	for (int& t: A) {
		cin >> t;
		mx = max(mx,t);
	}
 
	vector<int> cum(mx+1); for (int t: A) ++cum[t];
	for (int i = 1; i <= mx; ++i) cum[i] += cum[i-1];
	auto getCum = [&](int ind) { // number of elements of A <= ind
		if (ind > mx) return cum.back();
		return cum[ind];
	};
 
	long long ans = 0;
	for (int x = 1; x <= mx; ++x) {
		vector<int> counts{0};
		for (int t = 1; x*t <= mx; ++t)
			counts.push_back(getCum(x*(t+1)-1)-getCum(x*t-1));
		vector<int> odd; 
		for (int t = 1; t < counts.size(); ++t) 
			if (counts[t]&1) odd.push_back(t);
		if (odd == vector<int>{1} || (odd.size() == 2 && odd[0]+1 == odd[1]))
			ans += counts[odd.back()];
	}
	cout << ans << "\n";
}
