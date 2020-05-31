#include <bits/stdc++.h>

using namespace std;

constexpr size_t MAX_N = 100000;
int N;
int H[MAX_N];
int memo[MAX_N];

int cost(int i) {
  if (i == N-1) return 0;

  if (memo[i] != -1) return memo[i];

  if (!(i+2 < N)) {
    memo[i] = abs(H[i+1] - H[i]) + cost(i+1); 
    return memo[i];
  }

  memo[i] = min(
    abs(H[i+1] - H[i]) + cost(i+1),
    abs(H[i+2] - H[i]) + cost(i+2) 
  );

  return memo[i];
}

int main() {
  
  scanf("%d", &N);

  for (int i=0; i<N; i++) {
    memo[i] = -1;
  }

  for (int i=0; i<N; i++) {
    scanf("%d", &H[i]);
  }

  printf("%d\n", cost(0));
  
  return 0;
}
