#include <bits/stdc++.h>

using namespace std;

constexpr size_t N = 10000000;

vector<int>s;

int main() {
  
  s = vector<int>(N, -1);

  for (int i=2; i*i < N; i++) {
    if (s[i] != -1) continue;
    for (int j = i; j < N; j += i) {
      if (j > i) s[j] = i;
    }
  }

  int count = 0;
  for (int i=2;i<N;i++) {
    if (s[i] == -1) count += 1;
  }

  cout << count << endl;
  
  return 0;
}
