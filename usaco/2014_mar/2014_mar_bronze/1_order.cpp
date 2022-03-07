#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <utility>
#define MAX_N 102

using namespace std;

int N;
int A[MAX_N];
int B[MAX_N];
int P[MAX_N];
int considered[MAX_N];

set<int> current_cycle;
vector<pair<int, int> > AB;

int first_unconsidered() {
  for (int i = 1; i <= N; i++)
    if (considered[i] == 0)
      return i;
  return -1;
}

int main() {
  
  int i;

  freopen("reorder.in", "r", stdin);
  freopen("reorder.out", "w", stdout);

  scanf("%d", &N);
  for (i = 1; i <= N; i++) {
    scanf("%d", &A[i]);
  }
  for (i = 1; i <= N; i++) {
    scanf("%d", &B[i]);
  }
  for (i = 1; i <= N; i++) {
    AB.push_back(make_pair(A[i], B[i]));
  }
  sort(AB.begin(), AB.end());
  for (i = 1; i <= N; i++) {
    P[i] = AB[i-1].second;
  }

  int num_cycles = 0;
  int max_cycle_length = -1;

  while (int fc = first_unconsidered() != -1) {
    i = first_unconsidered();
    while (current_cycle.find(P[i]) ==  current_cycle.end()) {
      current_cycle.insert(P[i]);
      i = P[i];
      considered[i] = 1;
    }
    int cycle_length = current_cycle.size();
    if (cycle_length > 1) {
      num_cycles++;
      max_cycle_length = max(max_cycle_length, cycle_length);
    }
    current_cycle.clear();
  }
  printf("%d %d\n", num_cycles, max_cycle_length);
}