#include <stdio.h>
#include <string.h>

int N;
double P;
int T;

double memo[2001][2001];

double Z(int t, int n) {
	if (t == 0) {
		if (n == 0) {
			return 1;
		} else {
			return 0;
		}
	}
	if (memo[t][n] > -1) {
		return memo[t][n];
	}
	else if (n == N) {
		memo[t][n] = Z(t - 1, n) + Z(t - 1, n - 1) * P;
	} else {
		memo[t][n] = (Z(t - 1, n) * (1 - P)) + (Z(t - 1, n - 1) * P);
	}
	return memo[t][n];
}

int main() {
	scanf("%d %lf %d", &N, &P, &T);

	int i, j;
	for (i = 0; i < 2001; i++)
		for (j = 0; j < 2001; j++)
			memo[i][j] = -1;

	double S = 0;
	for (j = 1; j <= N; j++) {
		S += j * Z(T, j);
	}
	printf("%lf\n", S);
}