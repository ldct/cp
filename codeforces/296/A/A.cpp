#include <cstdio>

long long numships(long long a, long long b) {
	// printf("%ld %ld\n", a, b);
	// fflush(0);
	if (a == b) {
		return 1;
	} else if (a > b) {
		return numships(b, a);
	} else if (a == 0) {
		return 0;
	} else {
		return (b / a) + numships(b % a, a);
	}
}

int main() {

  long long a;
  long long b;

  scanf("%ld %ld", &a, &b);
  printf("%ld\n", numships(a, b));

  return 0;
}
