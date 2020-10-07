#pragma GCC optimize ("trapv")
#include <bits/stdc++.h>
using namespace std;

constexpr int MAX_N = 100009;
int N;

long long heights[MAX_N];
long long memo[MAX_N];
long long link[MAX_N];

long long sabs(long long x) { 
  return abs(x)*abs(x); 
}

int main() {

  cin >> N;

  for (int i=0; i<N; i++) {
    memo[i] = -1;
    cin >> heights[i];
  }

  for (int i=0; i<N-1; i++) {
    if (i == N-2) {
      link[i] = sabs(heights[i] - heights[i+1]);
    } else {
      link[i] = min(
        sabs(heights[i] - heights[i+1]),
        3*sabs(heights[i+2] - heights[i]) + sabs(heights[i+1] - heights[i+2])
      );
    }
  }

  for (int i=N-1; i!=-1; i--) {
    if (i == N-1) {
      memo[i] = 0;
    } else if (i == N-2) {
      memo[i] = link[i];
    } else {
      long long o1 = memo[i+1] + link[i];
      long long o2 = memo[i+2] + 3*sabs(heights[i] - heights[i+2]);
      memo[i] = min(o1, o2);    
    }
  }

  cout << memo[0] << endl;

  return 0;
}
