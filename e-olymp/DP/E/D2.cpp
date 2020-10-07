#include <bits/stdc++.h>
using namespace std;

constexpr int MAX_N = 100009;
int N;

int heights[MAX_N];
int best[MAX_N];
long long memo[MAX_N];

long long sabs(long long x) { return abs(x)*abs(x); }

long long ans(int i) {
  if (i == N-1) return 0;
  if (memo[i] != -1) return memo[i];
  if (i == N-2) {
    best[i] = i+1;
    return memo[i] = sabs(heights[i] - heights[i+1]);
  }
  long long o1 = ans(i+1) + sabs(heights[i] - heights[i+1]);
  long long o2 = ans(i+2) + 3*sabs(heights[i] - heights[i+2]);

  if (o1 < o2) {
    best[i] = i+1;
  } else {
    best[i] = i+2;
  }

  return memo[i] = min(o1, o2);    
}

int main() {

  cin >> N;

  for (int i=0; i<N; i++) {
    memo[i] = -1;
    cin >> heights[i];
  }

  cout << ans(0) << endl;

  return 0;
}