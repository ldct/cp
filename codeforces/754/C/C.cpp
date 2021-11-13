#include <bits/stdc++.h>
using namespace std;

int N;

bool good(string& S, int i, int j) {
    j = min(j, (int)S.size());
    if (j - i < 2) return false;
    int num_a = 0;
    int num_b = 0;
    int num_c = 0;
    for (int k=i; k<j; k++) {
        if (S[k] == 'a') num_a += 1;
        if (S[k] == 'b') num_b += 1;
        if (S[k] == 'c') num_c += 1;
    }
    return num_a > max(num_b, num_c);
}

int ans(string& S) {
  int r = 0;
  for (auto offset : {2,3,4,5,6,7}) {
    for (int i=0; i<S.size()+1; i++) {
      if (good(S, i, i+offset)) return offset;
    }
  }
  return -1;
}

int main() {

  cin >> N;
  for (int i=0; i<N; i++) {
    int l;
    cin >> l;
    string S;
    cin >> S;
    cout << ans(S) << endl;
  }

  return 0;
}
