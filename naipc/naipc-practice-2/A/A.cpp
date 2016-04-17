#include <cstdio>
#include <map>
#include <vector>
#include <utility>
#include <cstdlib>

using namespace std;

map<int, int> state;
map<int, vector<pair<int, int> > > neighbours;

int set_to_1 = 0;
int set_to_0 = 0;

int total_min_set_to_1 = 0;

void impossible(int c) {
  printf("impossible\n");
  exit(0);
}

void explore_implications(int a) {

  vector<pair<int, int> > my_neighbours = neighbours[a];
  for (int j = 0; j < my_neighbours.size(); j++) {
    pair<int, int> my_neighbour = my_neighbours[j];
    int b = my_neighbour.first;
    int c = my_neighbour.second;

    if (c == 2) {
      if (state[a] == 0 || state[b] == 0) {
        // 0 1
        // 0 -1
        // 0 0
        // 1 0
        // -1 0
        impossible(c);
      }
      if (state[a] == -1) {
        set_to_1++;
        state[a] = 1;
        explore_implications(a);
      }
      if (state[b] == -1) {
        set_to_1++;
        state[b] = 1;
        explore_implications(b);
      }
    }

    if (c == 0) {
      if (state[a] == 1 || state[b] == 1) {
        impossible(c);
      }
      if (state[a] == -1) {
        set_to_0++;
        state[a] = 0;
        explore_implications(a);
      }
      if (state[b] == -1) {
        set_to_0++;
        state[b] = 0;
        explore_implications(b);
      }
    }

    if (c == 1) {
      if (state[a] == 1 && state[b] == 1) {
        impossible(c);
      }
      if (state[a] == 0 && state[b] == 0) {
        impossible(c);
      }
      if (state[a] == 0 && state[b] == -1) {
        state[b] = 1;
        set_to_1++;
        explore_implications(b);
      }
      if (state[a] == -1 && state[b] == 0) {
        state[a] = 1;
        set_to_1++;
        explore_implications(a);
      }
      if (state[a] == 1 && state[b] == -1) {
        state[b] = 0;
        set_to_0++;
        explore_implications(b);
      }
      if (state[a] == -1 && state[b] == 1) {
        state[a] = 0;
        set_to_0++;
        explore_implications(a);
      }
      // 1, 0
      // 0, 1
      // -1, -1
    }
  }
}

int main() {

  int N, M;

  scanf("%d %d\n", &N, &M);

  for (int a = 1; a <= N; a++) {
    vector<pair<int, int> > v;
    neighbours[a] = v;
    state[a] = -1;
  }

  for (int i = 0; i < M; i++) {
    int a, b, c;
    scanf("%d %d %d\n", &a, &b, &c);
    neighbours[a].push_back(make_pair(b, c));
    neighbours[b].push_back(make_pair(a, c));
  }

  for (int a = 1; a <= N; a++) {
    explore_implications(a);
  }

  // for (int a = 1; a <= N; a++) {
  //   printf("%d %d\n", a, state[a]);
  // }

  total_min_set_to_1 = set_to_1;

  for (int a = 1; a <= N; a++) {

    if (state[a] == -1) {
      set_to_0 = 1;
      set_to_1 = 0;
      state[a] = 0;
      explore_implications(a);
      total_min_set_to_1 += min(set_to_0, set_to_1);
    }
  }

  printf("%d\n", total_min_set_to_1);

  return 0;
}
