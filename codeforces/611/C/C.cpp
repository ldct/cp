#include <iostream>
#include <map>
#include <utility>
#include <cstdio>

using namespace std;

const int MAX_HW = 520;

int h, w;
char grid[MAX_HW][MAX_HW];

bool isHGood(int r, int c) {
  if (c == w) {
    return false;
  } else {
    return grid[r-1][c-1] == '.' && grid[r-1][c] == '.';
  }
}

bool isVGood(int r, int c) {
  if (r == h) {
    return false;
  } else {
    return grid[r-1][c-1] == '.' && grid[r][c-1] == '.';
  }
}

int numHGoodMemo[MAX_HW][MAX_HW];

int numHGood(int r, int c) {

  if (numHGoodMemo[r][c] != -1)
    return numHGoodMemo[r][c];

  if (r <= 1) {
    int ans = 0;
    for (int x=1; x<=r; x++)
      for (int y=1; y<=c; y++)
        if (isHGood(x, y)) ans += 1;
    numHGoodMemo[r][c] = ans;
  } else {
    int ans = numHGood(r-1, c);
    for (int y=1; y<= c; y++) {
      if (isHGood(r, y)) ans += 1;
    }
    numHGoodMemo[r][c] = ans;
  }
  return numHGoodMemo[r][c];

}

int numVGoodMemo[MAX_HW][MAX_HW];
int numVGood(int r, int c) {
  if (numVGoodMemo[r][c] != -1)
    return numVGoodMemo[r][c];

  if (r <= 1) {
    int ans = 0;
    for (int x=1; x<=r; x++)
      for (int y=1; y<=c; y++)
        if (isVGood(x, y)) ans += 1;

    numVGoodMemo[r][c] = ans;
  } else {
    int ans = numVGood(r-1, c);
    for (int y=1; y<= c; y++) {
      if (isVGood(r, y)) ans += 1;
    }
    numVGoodMemo[r][c] = ans;
  }
  return numVGoodMemo[r][c];
}

int numHGood4(int r1, int c1, int r2, int c2) {
  return numHGood(r2, c2) - numHGood(r1-1, c2) - numHGood(r2, c1-1) + numHGood(r1-1, c1-1);
}

int numVGood4(int r1, int c1, int r2, int c2) {
  return numVGood(r2, c2) - numVGood(r1-1, c2) - numVGood(r2, c1-1) + numVGood(r1-1, c1-1);
}

int numDominoes(int r1, int c1, int r2, int c2) {
  return numHGood4(r1, c1, r2, c2-1) + numVGood4(r1, c1, r2-1, c2);
}

int main () {
  scanf("%d %d\n", &h, &w);

  for (int i=0; i<MAX_HW; i++) {
    for (int j=0; j<MAX_HW; j++) {
      numHGoodMemo[i][j] = -1;
      numVGoodMemo[i][j] = -1;
    }
  }

  for (int i=0; i<h; i++) {
    for (int j=0; j<w; j++) {
      scanf("%c", &grid[i][j]);
    }
    scanf("\n");
  }

  int q;
  scanf("%d\n", &q);

  for (int i=0; i<q; i++) {
    int r1, c1, r2, c2;
    scanf("%d %d %d %d\n", &r1, &c1, &r2, &c2);
    printf("%d\n", numDominoes(r1, c1, r2, c2));
  }

}