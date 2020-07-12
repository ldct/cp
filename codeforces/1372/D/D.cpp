#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 200009;

int N;
long long B[MAX_N];
long long* A_ptr = B;

long long memo[MAX_N][2][2];

long long ans(int start, bool p1, bool p2) {
  if (start == N) return 0;

  if (memo[start][p1][p2] != -1) return memo[start][p1][p2];

  if (p1 && p2) return memo[start][p1][p2] = ans(start+1, true, false);
  if (!p1 && p2) return memo[start][p1][p2] = max(
    ans(start+1, true, false),
    A_ptr[start] + ans(start+1, true, true)
  );
  if (!p2) return memo[start][p1][p2] = A_ptr[start] + ans(start+1, false, true);
}

int main() {
  
  cin >> N;

  for (int i=0; i<N; i++) {
    cin >> B[i];
  }

  long long ret = LLONG_MIN;

  for (int i=0; i<4; i++) {

    for (int n=0; n<N; n++) {
      memo[n][true][true] = -1;
      memo[n][true][false] = -1;
      memo[n][false][true] = -1;
      memo[n][false][false] = -1;
    }

    ret = max(ret, ans(0, true, true));
    ret = max(ret, ans(0, true, false));
    ret = max(ret, ans(0, false, true));
    ret = max(ret, ans(0, false, false));

    A_ptr[N] = A_ptr[0];
    A_ptr++;
  }

  cout << ret << endl;

  return 0;
}
