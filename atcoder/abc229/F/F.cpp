#include <bits/stdc++.h>
using namespace std;

int N;
long long spoke[200009];
long long right_cross[200009];

long long match(bool a, bool b) {
  if (a == b) return 0;
  return 1;
}

long long memo[200009][2][2];

long long ans(int i, bool first_colour, bool last_colour) {
  if (i == N) {
    return match(first_colour, last_colour)*right_cross[N-1];
  }
  if (memo[i][first_colour][last_colour] != -1) return memo[i][first_colour][last_colour];
  long long ret = -1;

  ret = max(ret, ans(i+1, first_colour, true) + match(last_colour, true)*right_cross[i-1] + spoke[i]);
  ret = max(ret, ans(i+1, first_colour, false) + match(last_colour, false)*right_cross[i-1]);
  return memo[i][first_colour][last_colour] = ret;

}

int main() {

  memset(memo, -1, sizeof(memo));

  long long total = 0;
  cin >> N;
  for (int i=0; i<N; i++) {
    cin >> spoke[i];
    total += spoke[i];
  }
  for (int i=0; i<N; i++) {
    cin >> right_cross[i];
    total += right_cross[i];
  }

  long long max_cut = max(
    (spoke[0] + ans(1, true, true)),
    ans(1, false, false)
  );

  cout << (total-max_cut) << endl;

  return 0;
}
