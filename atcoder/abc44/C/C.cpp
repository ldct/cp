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

int N, A;
vector<int> X;

int memo[51][51][50*50+1];

int ans(int i, int cnt, int total) {
  if (i == X.size()) {
    if (cnt == 0 && total == 0) return 1;
    return 0;
  }
  if (memo[i][cnt][total] != -1) return memo[i][cnt][total];
  return memo[i][cnt][total] = ans(i+1, cnt, total) + ans(i+1, cnt-1, total-X[i]);
}

i32 main() {

  memset(memo, -1, sizeof(memo));

  cin >> N >> A;
  for (int i=0; i<N; i++) {
    int x;
    cin >> x;
    X.push_back(x);
  }

  int ret = 0;
  for (int cnt=1; cnt<=X.size(); cnt++) {
    ret += ans(0, cnt, cnt*A);
  }
  cout << ret << endl;
  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS