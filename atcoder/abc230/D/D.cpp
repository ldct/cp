#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

int N, D;
vector<pair<int, int>> intervals;

int main() {

  cin >> N >> D;
  for (int i=0; i<N; i++) {
    int l, r;
    cin >> l >> r;
    intervals.push_back({l, r});
  }
  cout << N << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS