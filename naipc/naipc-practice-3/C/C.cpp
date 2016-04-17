#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX_n 31

int N;
char scoreboard[MAX_n][MAX_n];
char tmp_scoreboard[MAX_n][MAX_n];

void copy_scoreboard(int n) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      tmp_scoreboard[i][j] = scoreboard[i][j];
    }
  }
}

int main() {
  scanf("%d\n", &N);

  while(N--) {
    int n;

    scanf("%d\n", &n);

    char c;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        scanf("%c", &scoreboard[i][j]);
      }
      scanf("\n");
    }

    vector<int> p_winners;

    for (int p = 0; p < n; p++) {
      // printf("checking player %d\n", p);

      copy_scoreboard(n);

      for (int i = 0; i < n; i++) {
        if (tmp_scoreboard[p][i] == '.') {
          tmp_scoreboard[p][i] = '1';
          tmp_scoreboard[i][p] = '0';
        }
      }

      // for (int i = 0; i < n; i++) {
      //   for (int j = 0; j < n; j++) {
      //     printf("%c", tmp_scoreboard[i][j]);
      //   }
      //   printf("\n");
      // }

      int d_score = 0;
      for (int i = 0; i < n; i++) {
        if (tmp_scoreboard[p][i] == '1') {
          d_score += 2;
        } else if (tmp_scoreboard[p][i] == 'd') {
          d_score += 1;
        }
      }

      int max_op_d_score = 0;
      // printf("player's score is %d\n", d_score);


      for (int o_p = 0; o_p < n; o_p++) {
        if (o_p == p) {
          continue;
        }
        int op_d_score = 0;
        for (int i = 0; i < n; i++) {
          if (tmp_scoreboard[o_p][i] == '1') {
            op_d_score += 2;
          } else if (tmp_scoreboard[o_p][i] == 'd') {
            op_d_score += 1;
          } else if (tmp_scoreboard[o_p][i] == '.') {
            op_d_score += 1;
          }
        }
        max_op_d_score = max(op_d_score, max_op_d_score);
      }
      if (d_score >= max_op_d_score) {
        p_winners.push_back(p + 1);
        // printf("%d ", p + 1);
      }
    }
    for (int i = 0; i < p_winners.size() - 1; i++) {
      printf("%d ", p_winners[i]);
    }
    printf("%d", p_winners[p_winners.size() - 1]);
    if (N != 0) {
      printf("\n");
    }
  }


  return 0;
}
