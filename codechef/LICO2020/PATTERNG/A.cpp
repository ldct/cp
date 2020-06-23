#include <bits/stdc++.h>

using namespace std;

long long N;
string S;
long long SLEN;

map<char, vector<long long>> freqs;

long long ans(long long R, char C) {
    long long complete = R / SLEN;
    long long ret = freqs[C][SLEN];

    long long i = ((unsigned __int128)R*(R-1) / 2) % SLEN;
    long long j = (i + R) % SLEN;

    // cout << "i=" << i << " j=" << j << endl;

    if (i == j) {
      return complete*ret;
    } else if (i < j) {
      return complete*ret + freqs[C][j] - freqs[C][i];
    } else {
      long long end = freqs[C][SLEN] - freqs[C][i];
      long long start = freqs[C][j];
      return complete*ret + end + start;
    }
}

int main() {
  
  cin >> N;
  cin >> S;

  SLEN = S.length();

  for (char c = 'A'; c <= 'Z'; c++) {
    freqs[c] = vector<long long>(SLEN+1, 0);
  }
  for (long long i=0; i<SLEN; i++) {
    assert('A' <= S[i] && S[i] <= 'Z');
    freqs[S[i]][i+1] = 1;
  }
  for (char c = 'A'; c <= 'Z'; c++) {
    for (long long i=1; i<=SLEN; i++) {
      freqs[c][i] += freqs[c][i-1];
    }
  }

  long long Q;
  cin >> Q;

  for (long long i=0; i<Q; i++) {
    long long R;
    char C;
    cin >> R >> C;

    assert('A' <= C && C <= 'Z');

    cout << ans(R, C) << endl;

  }

}
