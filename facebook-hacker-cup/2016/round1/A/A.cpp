#include <iostream>
#include <cassert>

using namespace std;

const int MAX_N = 100010;

int T;
int N;
int W[MAX_N];

int plusInf(int a, int b) {
	if (a == -1 || b == -1) return -1;
	return a + b;
}

int min2(int a, int b) {
	if (a == -1) return b;
	if (b == -1) return a;
	if (a < b) return a;
	return b;
}

int min3(int a, int b, int c) {
	return min2(a, min2(b, c));
}

int min4(int a, int b, int c, int d) {
	return min2(min2(a, b), min2(c, d));
}

int mA2(int a, int b) {
	// number of ways to pad [a, b] into a contest
	int gap = b-a;
	if (gap <= 0) return -1;
	if (gap > 30) return -1;
	return 2;
}

bool okGap(int gap) {
	return 0 < gap && gap <= 10;
}

int mA4(int a, int b, int c, int d) {
	int g1 = b-a;
	int g2 = c-b;
	int g3 = d-c;

	if (!okGap(g1)) return -1;
	if (!okGap(g2)) return -1;
	if (!okGap(g3)) return -1;

	if (a < 1) return -1;
	if (d > 100) return -1;

	return 0;
}

int mA3(int a, int b, int c) {
	int g1 = b-a;
	int g2 = c-b;	
	if (g1 <= 0) return -1;
	if (g2 <= 0) return -1;
	if (g1 > 20) return -1;
	if (g2 > 20) return -1;
	// a < b < c
	return plusInf(1, min4(
		mA4(a-1, a, b, c),
		mA4(a, (a+b)/2, b, c),
		mA4(a, b, (b+c)/2, c),
		mA4(a, b, c, c+1)
	));

}

int memo[MAX_N];

int mA(int s) {

	if (memo[s] != -1) return memo[s];

	int num = N - s;
	if (num == 0) return 0;
	if (num == 1) return 3;
	if (num == 2) {
		memo[s] = min2(
			plusInf(3, mA(s+1)),
			plusInf(mA2(W[s], W[s+1]), mA(s+2))
		);
	} else if (num == 3) {
		memo[s] = min3(
			plusInf(3, mA(s+1)),
			plusInf(mA2(W[s], W[s+1]), mA(s+2)),
			plusInf(mA3(W[s], W[s+1], W[s+2]), mA(s+3))
		);
	} else {
		memo[s] = min4(
			plusInf(3, mA(s+1)),
			plusInf(mA2(W[s], W[s+1]), mA(s+2)),
			plusInf(mA3(W[s], W[s+1], W[s+2]), mA(s+3)),
			plusInf(mA4(W[s], W[s+1], W[s+2], W[s+3]), mA(s+4))
		);
	}
	return memo[s];
}

int main () {
	cin >> T;

	for (int t=0; t<T; t++) {
		cin >> N;
		for (int n=0; n<N; n++) {
			cin >> W[n];
		}
		for (int n=0; n<=N; n++) {
			memo[n] = -1;
		}
		cout << "Case #" << t + 1 << ": " << mA(0) << endl;
	}
}