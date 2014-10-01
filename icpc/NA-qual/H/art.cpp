#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int N, k;
int value[201][2];

int LEFT = 0;
int RIGHT = 1;
int NONE = 2;

long long int memo_min_close[204][3][204];

//minimum cost to close k galleries in rows [0, row)
long long int min_close(int row, int previous_closed, int k) {

  if (k == 0) {
    return 0;
  }
  if (row == 0) {
    return 100 * 200 * 2 * 2;
  }

  if (memo_min_close[row][previous_closed][k] != -1) {
   return memo_min_close[row][previous_closed][k];
  }

  long long int min_so_far = 100 * 200 * 2 * 2 * 2;

  //try to close neither
  min_so_far = min(min_so_far, min_close(row - 1, NONE, k));

  //try to close left
  if (previous_closed == NONE || previous_closed == LEFT) {
    min_so_far = min(min_so_far, value[row - 1][LEFT] + min_close(row - 1, LEFT, k - 1));
  }

  //try to close right
  if (previous_closed == NONE || previous_closed == RIGHT) {
    min_so_far = min(min_so_far, value[row - 1][RIGHT] + min_close(row - 1, RIGHT, k - 1));
  }

  memo_min_close[row][previous_closed][k] = min_so_far;
  return min_so_far;
}

int main() {

  while (1) {
    scanf("%d %d", &N, &k);

    if (N == 0 && k == 0) {
      return 0;
    }

    int total_value = 0;
    for (int i=0; i<N; i++) {
      scanf("%d %d", &value[i][0], &value[i][1]);
      total_value += (value[i][0] + value[i][1]);
    }

    memset(memo_min_close, -1, sizeof(memo_min_close));

    printf("%lld\n", total_value - min_close(N, NONE, k));
  }



  return 0;
}
