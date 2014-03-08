#include <cstdio>
#define MAX_N 1000

int N, height[MAX_N];

int main() {

  scanf("%d", &N);

  int sum=0;
  for (int i=0; i<N; i++) {
    scanf("%d", &height[i]);
    sum += height[i];
  }

  int mean = sum / N;

  int answer = 0;
  for (int i=0; i<N; i++) {
    if (height[i] > mean) {
      answer += height[i] - mean;
    }
  }

  printf ("%d\n", answer);

  return 0;
}