#include <bits/stdc++.h>
using namespace std;

constexpr int MAX_N = 100009;
int N;

int heights[MAX_N];
int best[MAX_N];
int memo[MAX_N];

long long ans(int i) {
  if (i == N-1) return 0;
  if (memo[i] != -1) return memo[i];
  if (i == N-2) {
    best[i] = i+1;
    return memo[i] = abs(heights[i] - heights[i+1]);
  }
  long long o1 = ans(i+1) + abs(heights[i] - heights[i+1]);
  long long o2 = ans(i+2) + 3*abs(heights[i] - heights[i+2]);

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

  vector<int> pos;

  for (int i=0; i != N-1; i = best[i]) {
    pos.push_back(i+1);
  }
  pos.push_back(N);

  cout << pos.size() << endl;
  for (int i=0; i < pos.size()-1; i++) {
    cout << pos[i] << " ";
  }
  cout << pos[pos.size()-1] << endl;
   
  return 0;
}
