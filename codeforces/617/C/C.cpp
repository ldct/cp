#include <iostream>
#include <queue>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

int N;
ll X1, Y1, X2, Y2;

vector<pair<ll, ll>> points;

ll dist2(ll dx, ll dy) {
	return dx*dx + dy*dy;
}

int main () {
	cin >> N >> X1 >> Y1 >> X2 >> Y2;

	for (int n=0; n<N; n++) {
		ll x, y;
		cin >> x >> y;
		ll r1 = dist2(y - Y1, x - X1);
		ll r2 = dist2(y - Y2, x - X2);
		points.push_back(make_pair(r1, r2));
	}

	sort(points.begin(), points.end(), greater<pair<ll, ll>>());

	ll ans = -1;
	for (int i=0; i<=N; i++) {

		ll r1;
		if (i < N) {
			auto point = points[i];
			r1 = point.first;
		} else {
			r1 = 0;
		}
		
		ll maxR2 = 0;
		for (int j=0; j<i; j++) {
			maxR2 = max(maxR2, points[j].second);
		}

		ll candidate = r1 + maxR2;

		if (ans == -1) ans = candidate;
		ans = min(ans, candidate);
	}

	cout << ans << endl;
}