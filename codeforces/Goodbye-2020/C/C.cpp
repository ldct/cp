#include <bits/stdc++.h>
using namespace std;

int min3(int a, int b, int c) { return min(a, min(b, c)); }

constexpr int MAX_N = 100009;
int T;
char characters[MAX_N];
char reduced[MAX_N];
int N;
int memo[5][5][MAX_N];

bool ok(char t, char p, char q, char r, char s) {
  if (t == p) return false;
  if (t == q) return false;
  if (t == r) return false;
  if (t == s) return false;
  return true;
}

char exclude(char p, char q, char r, char s) {
  for (char ret = 'a'; ret != 'z'; ret++) {
    if (ok(ret, p, q, r, s)) return ret;
  }
  assert(false);
}

int dp(char p, char q, int i) {
  assert('a' <= p && p <= 'e');
  assert('a' <= q && q <= 'e');
  assert(p != q);
  if (i == N) return 0;
  if (memo[p - 'a'][q - 'a'][i] != -1) return memo[p - 'a'][q - 'a'][i];
  char n1 = exclude(p, q, '?', '?');
  char n2 = exclude(p, q, n1, '?');
  char n3 = exclude(p, q, n1, n2);

  return memo[p - 'a'][q - 'a'][i] = min3(
    (reduced[i] == n1 ? 0 : 1) + dp(q, n1, i+1),
    (reduced[i] == n2 ? 0 : 1) + dp(q, n2, i+1),
    (reduced[i] == n3 ? 0 : 1) + dp(q, n3, i+1)
  );
}

void ans() {
  for (int p=0; p<5; p++) for (int q=0; q<5; q++) for (int i=0; i<N; i++) memo[p][q][i] = -1;
  for (int i=0; i<N; i++) {
    int p = '?';
    int q = '?';
    int rp = '?';
    int rq = '?';

    if (i-2 >= 0) {
      p = characters[i-2];
      rp = reduced[i-2];
    }
    if (i-1 >= 0) {
      q = characters[i-1];
      rq = reduced[i-1];
    }

    if (characters[i] == p) {
      reduced[i] = rp;
    } else if (characters[i] == q) {
      reduced[i] = rq;
    } else {
      reduced[i] = exclude(rp, rq, '?', '?');
    }
  }
  // for (int i=0; i<N; i++) {
  //   cout << reduced[i];
  // }
  char p = exclude(reduced[0], '?', '?', '?');
  char q = exclude(reduced[0], p, '?', '?');
  cout << dp(p, q, 0) << endl;
}


int main() {

  cin >> T;
  while (T--) {
    string S;
    cin >> S;
    N = S.size();
    strcpy(characters, S.c_str());
    ans();
  }

  return 0;
}
