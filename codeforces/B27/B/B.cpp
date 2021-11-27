#include <bits/stdc++.h>
using namespace std;

// https://codeforces.com/contest/27/problem/E

constexpr size_t MAX_N = 5000000;

int s[MAX_N];

int main() {

  for (int i=1; i<MAX_N; i++)
    for (int j=i; j<MAX_N; j+=i) s[j] += 1;

  int N;
  cin >> N;

  for (int i=0; i<MAX_N; i++) {
    if (s[i] == N) {
      cout << i << endl;
      break;
    }
  }

  return 0;
}
