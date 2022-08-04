#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>

using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int N;
int A[300009];

int memo0[300009];
int memo1[300009];

int ans(int i) {
  // cost to feed [i, N)
  if (i >= N) return 0;

  if (memo0[i] != -1) return memo0[i];

  if (i > 0) return memo0[i] = min(
    A[i] + ans(i+2),
    A[i-1] + ans(i+1)
  );

  return memo0[i] = A[i] + ans(i+2);
}

int ans_short(int i) {
  // cost to feed [i, N-1)
  if (i >= N-1) return 0;

  if (memo1[i] != -1) return memo1[i];

  if (i > 0) return memo1[i] = min(
    A[i] + ans_short(i+2),
    A[i-1] + ans_short(i+1)
  );

  return memo1[i] = A[i] + ans_short(i+2);
}

i32 main() {

  memset(memo0, -1, sizeof(memo0));
  memset(memo1, -1, sizeof(memo1));

  cin >> N;
  for (int i=0; i<N; i++) {
    cin >> A[i];
  }

  cout << min(
    ans(0),
    A[N-1] + ans_short(1)
  ) << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS