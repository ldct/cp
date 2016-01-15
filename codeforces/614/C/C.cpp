#include <iostream>
#include <cmath>

const double PI = 3.1415926535897932384626433832795028841972;
const int MAX_N = 1000010;

using namespace std;

int N;
int Px, Py;

typedef long long ll;

ll R2 = 0;
double r2 = 1e100;

int X[MAX_N];
int Y[MAX_N];

ll dist2(ll ax, ll ay, ll bx, ll by) {
	ll x = abs(ax - bx);
	ll y = abs(ay - by);
	return x*x + y*y;
}

double nearestDistance2(ll ax, ll ay, ll bx, ll by) {

	// nearest distance2 between (a, b) and P

	ll PA2 = dist2(ax, ay, Px, Py);
	ll PB2 = dist2(bx, by, Px, Py);
	ll AB2 = dist2(ax, ay, bx, by);

	bool aObtuse = PB2 > PA2 + AB2;
	bool bObtuse = PA2 > AB2 + PB2;

	if (aObtuse || bObtuse) {
		return static_cast<double>(min(PA2, PB2));
	}

	ll PAx = ax - Px;
	ll PAy = ay - Py;
	ll PBx = bx - Px;
	ll PBy = by - Py;

	ll area = abs(PAx*PBy - PAy*PBx);

	// cout << "area=" << area << endl;

	// h * 0.5 * AB = area
	double h = static_cast<double>(area)/sqrt(AB2);

	// cout << "h=" << h << endl;
	return h*h;

}

int main() {
	cin >> N >> Px >> Py;

	for (int i=0; i<N; i++) {
		cin >> X[i] >> Y[i];
	}

	for (int i=0; i<N; i++) {
		R2 = max(R2, dist2(X[i], Y[i], Px, Py));
	}

	// cout << R2 << endl;

	for (int i=0; i<N; i++) {
		int j=(i+1)%N;
		r2 = min(r2, nearestDistance2(X[i], Y[i], X[j], Y[j]));
	}

	cout.precision(17);
	cout << fixed << PI * (static_cast<double>(R2) - r2) << endl;

}