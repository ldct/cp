#include <cstdio>
#include <map>
#define MAX_N 100001

typedef unsigned long long ull;

using namespace std;

int N, K;
map<int, ull> g_at_x;
map<int, ull> total_g_at_x;

ull g_if_end_x(int end_x) {
  int start_x = end_x - (2 * K);
  int floor_sx = MAX_N+2;
  for (map<int, ull>::reverse_iterator j = total_g_at_x.rbegin(); j != total_g_at_x.rend(); j++) {
    int x = j->second;
    if (x < start_x) {
      floor_sx = x;
      break;
    }
  }
  if (floor_sx == MAX_N + 2) {
    return total_g_at_x[end_x];
  } else {
    return total_g_at_x[end_x] - total_g_at_x[floor_sx];
  }
}

int main() {
  int g,x,i;

  freopen("lazy.in", "r", stdin);
  freopen("lazy.out", "w", stdout);

  scanf("%d %d", &N, &K);
  
  for (i = 0; i < N; i++) {
    scanf("%d %d", &g, &x);
    g_at_x[x] = g;
  }


  int old_x = -1;
  for (map<int, ull>::iterator j = g_at_x.begin(); j != g_at_x.end(); j++) {
    int x = j->first;
    int g = j->second;
    if (old_x == -1) {
      total_g_at_x[x] = g_at_x[x];
    } else {
      total_g_at_x[x] = total_g_at_x[old_x] + g_at_x[x];
    }
    old_x = x;
  }

  ull max_giex = 0;
  for (map<int, ull>::iterator j = g_at_x.begin(); j != g_at_x.end(); j++) {
    max_giex = max(max_giex, g_if_end_x(j->first));
  }
  printf("%llu\n", max_giex);

  return 0;
}
