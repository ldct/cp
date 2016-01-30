#include <iostream>
#include <cassert>
#include <utility>

using namespace std;

const int MAX_SIZE = 1100;
int M, N;
char C;
char frame1[MAX_SIZE][MAX_SIZE];
char frame2[MAX_SIZE][MAX_SIZE];
char frame3[MAX_SIZE][MAX_SIZE];

void printFrame(char frame[MAX_SIZE][MAX_SIZE]) {
  for (int i=0; i<M; i++) {
    for (int j=0; j<N; j++) {
      cout << frame[i][j];
    }
    cout << endl;
  }
}

char bgChar(char c1, char c2) {
  if (c1 != C) return c1;
  if (c2 != C) return c2;
  assert(false);
}

void computeFrame3Bg() {
  char c1, c2;
  for (int i=0; i<M; i++) {
    for (int j=0; j<N; j++) {
      c1 = frame1[i][j];
      c2 = frame2[i][j];
      if (c1 == C && c2 == C) assert(false);
      frame3[i][j] = bgChar(frame1[i][j], frame2[i][j]);
    }
  }
}

pair<int, int> topLeft(char frame[MAX_SIZE][MAX_SIZE]) {
  for (int i=0; i<M; i++) {
    for (int j=0; j<N; j++) {
      if (frame[i][j] == C) return make_pair(i, j);
    }
  }
  return make_pair(-1, -1);
}

void drawIfInBound(int x, int y) {
  if (0 <= x && x < M && 0 <= y && y < N) frame3[x][y] = C;
}

void extrapolate(int dx, int dy) {
  for (int i=0; i<M; i++) {
    for (int j=0; j<N; j++) {
      if (frame1[i][j] == C) {
        drawIfInBound(i + dx, j + dy);
      }
    }
  }
}

int main() {
  
  while (1) {
    string s;
    cin >> M >> N;
    getline(cin, s);
    C = s[2];

    if (M == 0 && N == 0 && C == ' ') return 0;

    for (int i=0; i<M; i++) {
      getline(cin, s);
      for (int j=0; j<N; j++) {
        frame1[i][j] = s[j];
      }
    }
    getline(cin, s);
    for (int i=0; i<M; i++) {
      getline(cin, s);
      for (int j=0; j<N; j++) {
        frame2[i][j] = s[j];
      }
    }
    getline(cin, s);

    computeFrame3Bg();

    pair<int, int> tl1 = topLeft(frame1);
    pair<int, int> tl2 = topLeft(frame2);

    pair<int, int> delta = make_pair(
      2*(tl2.first - tl1.first),
      2*(tl2.second - tl1.second)
    );

    extrapolate(delta.first, delta.second);


    // cout << endl << endl;
    // cout << "M=" << M << " N=" << N << " C=" << C << endl;
    // cout << "delta=" << "(" << delta.first << "," << delta.second << ")" << endl;
    printFrame(frame3);
    cout << endl;

  }

}
