#include <cstdio>
#include <cmath>

long long N;
long long MAX_C = 25;

int main() {

  scanf("%lld", &N);
  long long num_letters = ceil((float) N / MAX_C) + 1;

  return 0;
}
