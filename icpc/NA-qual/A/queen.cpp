#include <cstdio>
#include <cstdlib>

bool invalid = false;

int main() {

  char board[8][8];
  int queen[8];

  for (int i=0; i<8; i++) {
    queen[i] = -1;
  }

  for (int i=0; i<8; i++) {
    for (int j=0; j<8; j++) {
      scanf("%c", &board[i][j]);
      if (board[i][j] == '*') {
        if (queen[i] == -1) {
          queen[i] = j;
        } else {
          invalid = true;
        }
      }
    }
    scanf("\n");
  }

  for (int i=0; i<8; i++) {
    if (queen[i] == -1) {
      invalid = true;
    }
  }

  for (int i=0; i<8; i++) {
    for (int j=0; j<i; j++) {
      //i, queen[i]
      //j, queen[j]

      if (queen[i] == queen[j]) {
        invalid = true;
      }
      if (abs(i-j) == abs(queen[i] - queen[j])) {
        invalid = true;
      }
    }
  }

  if (invalid) {
    printf("invalid");
  } else {
    printf("valid");
  }

  return 0;
}
