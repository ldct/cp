#include <bits/stdc++.h>
using namespace std;

int eval(string& S, int assignments) {
  int ret = 0;
  int curr = 1;
  int mask = 0;
  for (int i=0; i<S.size(); i++) {
    char s = S[i];
    if ((s == '^') || (s == '&') || (s == '(')) continue;
    if (s == ')') {
      ret ^= curr;
      curr = 1;
      continue;
    }
    if (s == '!') {
      mask = 1;
      continue;
    }
    s -= 'a';
    assert(0 <= s && s < 15);
    curr &= ((bool) (assignments & (1 << s))  ^ mask);
    mask = 0;
  }
  return ret;
}

int ans(int K, string& S) {
  int ret = 0;
  for (int i=0; i<(1<<K); i++) {
    ret += eval(S, i);
  }
  return ret;
}

int main() {

  int T = 0;
  cin >> T;
  while (T --> 0) {
    int K;
    string S;
    cin >> K >> S;
    cout << ans(K, S) << endl;
  }

  return 0;
}
