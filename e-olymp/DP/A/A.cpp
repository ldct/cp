#include <bits/stdc++.h>
using namespace std;

int N;

long long ans(int i, int a, int b) {
  if (i == N) return 1;
  if (a == b && a != -1) return ans(i+1, a, 1-a);
  return ans(i+1, b, 0) + ans(i+1, b, 1);
}

int main() {
  
  for (int i=1; i<30; i++) {
    N = i;
    cout << i << " " << ans(0, -1, -1) << endl;
  }
    
  return 0;
}
