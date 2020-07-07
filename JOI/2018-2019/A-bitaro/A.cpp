#include <bits/stdc++.h>

constexpr size_t MAX_H = 3001;
constexpr size_t MAX_W = 3001;

char S[MAX_H][MAX_W];
int I_count[MAX_H][MAX_W];
int O_count[MAX_H][MAX_W];
int H;
int W;

using namespace std;

int main() {
  
  cin >> H >> W;
  char s;

  for (int x=0; x<H; x++) {
    for (int y=0; y<W; y++) {
      cin >> s;
      assert(s == 'J' || s == 'O' || s == 'I');
      S[H-1-x][W-1-y] = s;
    }
  }

  for (int y=0; y<W; y++) {
    int count=0;
    for (int x=0; x<H; x++) {
      if (S[x][y] == 'I') count += 1;
      I_count[x][y] = count;
    }
  }

  for (int x=0; x<H; x++) {
    int count=0;
    for (int y=0; y<W; y++) {
      if (S[x][y] == 'O') count += 1;
      O_count[x][y] = count;
    }
  }

  // for (int x=0; x<H; x++) {
  //   for (int y=0; y<W; y++) {
  //     cout << I_count[x][y];
  //   }
  //   cout << endl;
  // }


  long long ans = 0;

  for (int x=0; x<H; x++) {
    for (int y=0; y<W; y++) {
      if (S[x][y] == 'J') {
        ans += O_count[x][y] * I_count[x][y];
      }
    }
  }

  cout << ans << endl;

  return 0;
}
