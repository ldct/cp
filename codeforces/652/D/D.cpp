#include <bits/stdc++.h>

using namespace std;

constexpr size_t MAX_N = 2000001;
constexpr long long MODULUS = (1e9 + 7);

int memoT[MAX_N];
int memoF[MAX_N];

int ans(int i, bool disallow_occupy) {
  if (i <= 2) return 0;
  if (i == 3) {
    if (disallow_occupy) return 0;
    return 4;
  }
  if (i == 4) return 4;

  if (disallow_occupy && memoT[i] != -1) return memoT[i];
  if (!disallow_occupy && memoF[i] != -1) return memoF[i];

  int choice1 = (2LL*ans(i-2, true) + ans(i-1, true) + 4) % MODULUS;

  if (disallow_occupy) choice1 = -999;

  int choice2 = (2LL*ans(i-2, false) + ans(i-1, false)) % MODULUS;
  choice2 = choice2 % MODULUS;

  if (disallow_occupy) {
    return memoT[i] = choice2;
  } else {
    return memoF[i] = max(choice1, choice2);
  }

}

int main() {
  
  for (int i=0; i<MAX_N; i++) {
    memoT[i] = -1;
    memoF[i] = -1;
  }
  for (int i=5; i<MAX_N; i++) {
    ans(i, true);
    ans(i, false);
  }

  int T;

  cin >> T;

  while (T --> 0) {
    int n;
    cin >> n;
    cout << " " << max(ans(n, true), ans(n, false)) << endl;    
  }  
  return 0;
}
