#include <bits/stdc++.h>
using namespace std;

int X, Y;
string S;
long long memo[2][1009];

int idx(char c) {
    if (c == 'J') return 0;
    if (c == 'C') return 1;
    assert(false);
}

long long match(char a, char b) {
    assert(a == 'J' || a == 'C');
    assert(b == 'J' || b == 'C');
    if (a == 'C' && b == 'J') return X;
    if (a == 'J' && b == 'C') return Y;
    assert(a == b);
    return 0;
}

long long ans(int i, char last) {
    if (i == S.size()) return 0;
    if (last == '^') {
        if (S[i] == 'J') return ans(i+1, 'J');
        if (S[i] == 'C') return ans(i+1, 'C');
        return min(
            ans(i+1, 'J'),
            ans(i+1, 'C')
        );
    }
    if (memo[idx(last)][i] != -1) return memo[idx(last)][i];

    if (S[i] == '?') {
        return memo[idx(last)][i] = min(
            match(last, 'J') + ans(i+1, 'J'),
            match(last, 'C') + ans(i+1, 'C')
        );
    }
    assert(S[i] == 'J' || S[i] == 'C');
    return memo[idx(last)][i] = match(last, S[i]) + ans(i+1, S[i]);
}

int main() {

  int T;

  cin >> T;

  for (int i=1; i<=T; i++) {
    memset(memo, -1, sizeof(memo));
    cin >> X >> Y >> S;
    cout << "Case #" << i << ": " << ans(0, '^') << endl;
  }

  return 0;
}
