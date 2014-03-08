#include <cstdio>
#include <vector>
#include <cmath>
#include <cstring>

using namespace std;
typedef vector<int> vi;

#define MAX_N 20000
int N;
int A[MAX_N];
bool on_main_path[MAX_N];
bool main_path_cycle;
int on_cycle[MAX_N];
int memo_dtm[MAX_N];
int memo_dte[MAX_N];

int main_path_length = -1;
void set_main_path(int i) { //set main_path to 0
  main_path_length++;
  if (i == -1)
    return;
  if (on_main_path[i]) {
    main_path_cycle = true;
    return;
  }
  on_main_path[i] = true;
  set_main_path(A[i]);
}

int set_on_cycle(int i) {
  if (i == -1)
    return false;
  if (on_cycle[i] == 2) //visited
    return true;
  on_cycle[i] = 2;
  if (set_on_cycle(A[i]))
    return on_cycle[i] = true;
  else
    return on_cycle[i] = false;
}

int dist_to_main(int i) {
  if (on_cycle[i])
    return -MAX_N;
  if (i == 0)
    return -MAX_N;
  if (on_main_path[i])
    return 0;
  if (A[i] == -1)
    return -MAX_N;
  if (memo_dtm[i] > 0)
    return memo_dtm[i];
  return memo_dtm[i] = dist_to_main(A[i]) + 1;
}

int dist_to_end(int i) {
  if (on_cycle[i])
    return -MAX_N;
  if (on_main_path[i])
    return -MAX_N;
  if (A[i] == -1)
    return 1;
  if (memo_dte[i] > 0)
    return memo_dte[i];
  return memo_dte[i] = dist_to_end(A[i]) + 1;
}

int main() {
  scanf("%d", &N);

  for (int i=0; i<N; i++) {
    scanf("%d", &A[i]);
  }
  set_main_path(0);
  for (int i=0; i<N; i++)    
    set_on_cycle(i);

  memset(memo_dtm, -1, sizeof(memo_dtm));
  memset(memo_dte, -1, sizeof(memo_dte));

  int m = 0;
  if (main_path_cycle) {
    for (int i = 0; i < N; i++)
      m = max(m, dist_to_end(i));
  } else {
    for (int i = 0; i < N; i++) {
      m = max(m, dist_to_end(i));
      m = max(m, dist_to_main(i));
    }
  }
  printf("%d\n", main_path_length + m);
}
