#include <bits/stdc++.h>
using namespace std;

vector<long long> A;

bool ans(int start) {
  if (start == A.size() - 1) return true;
  // cout << "start=" << start << " " << A.size() << endl;
  bool next_winner = ans(start+1);
  if (next_winner) {
    return (A[start] > 1);
  } else {
    return true;
  }
}

int main() {
  
  int T;
  cin >> T;

  while (T --> 0) {
    A.clear();
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
      long long a;
      cin >> a;
      A.push_back(a);
    }
    if (ans(0)) {
      cout << "First" << endl;
    } else {
      cout << "Second" << endl;
    }
  }    
  return 0;
}
