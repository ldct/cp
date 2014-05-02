#include <cstdio>
#include <utility>
#include <queue>
#include <map>
#include <vector>
#include <set>
#include <algorithm>

#define MAX_N 10
#define MAX_HW 500

using namespace std;

int N, W, H;
char grid[MAX_HW][MAX_HW];
pair<int, int> initial_position[MAX_N];
map<pair<int, int>, int> dist[MAX_N];

int ctoi(char c) {
  if (c == '1') return 1;
  if (c == '2') return 2;
  if (c == '3') return 3;
  if (c == '4') return 4;
  if (c == '5') return 5;
  if (c == '6') return 6;
  if (c == '7') return 7;
  if (c == '8') return 8;
  if (c == '9') return 9;
  return -1;
}

pair<int, int> ending_place_timeout(int x, int y, int dx, int dy, int timeout) { //todo: limit
  
  //printf("%d %d\n", x, y);
  if (timeout == 0) {
    return make_pair(-1, -1);
  }

  int next_x, next_y;
  int new_dx, new_dy;

  if (grid[x][y] == 'A') {
    new_dx = dy;
    new_dy = -dx;
  } else if (grid[x][y] == 'C') {
    new_dx = -dy;
    new_dy = dx;
  } else {
    new_dx = dx;
    new_dy = dy;
  }
  next_x = x + new_dx;
  next_y = y + new_dy;

  if (next_x < 0 || next_x >= W || next_y < 0 || next_y >= H || grid[next_x][next_y] == 'x') {
    return make_pair(x, y);
  } else {
    return ending_place_timeout(next_x, next_y, new_dx, new_dy, timeout - 1);
  }
}

pair<int, int> ending_place(int x, int y, int dx, int dy) {
  return ending_place_timeout(x, y, dx, dy, N*W + 1);
}

void bfs(int robot_id) {
  queue<pair<int, int> > q;
  pair<int, int> s = initial_position[robot_id];
  q.push(s);

  dist[robot_id][s] = 0;

  while (!q.empty()) {
    pair<int, int> u = q.front(); q.pop();

    int x = u.first;
    int y = u.second;

    //printf("visit robot %d layer %d, (%d, %d)\n", robot_id, dist[robot_id][u], x, y);
    pair<int, int> ds[4] = {make_pair(0,1), make_pair(0,-1), make_pair(1,0), make_pair(-1,0)};

    for (int i=0; i<4; i++) {
      int dx = ds[i].first;
      int dy = ds[i].second;

      pair<int, int> neighbour = ending_place(x, y, dx, dy);
      if (neighbour.first != -1 && !dist[robot_id].count(neighbour)) {
        dist[robot_id][neighbour] = dist[robot_id][u] + 1;
        q.push(neighbour);
      }
    }
  }
}

vector<vector<int> > unordered_partitions(int N, int p) {
  if (p == 1) {
    vector<int> singleton; 
    vector<vector<int> > ret;
    singleton.push_back(N);
    ret.push_back(singleton);
    return ret;
  } else {
    vector<vector<int> > ret;
    for (int i=0; i<=N; i++) {
      vector<vector<int> > solutions = unordered_partitions(N - i, p - 1);
      for (int j=0; j<solutions.size(); j++) {
        solutions[j].push_back(i);
        ret.push_back(solutions[j]);
      }
    }
    return ret;
  }
}

int main() {
  
  scanf("%d %d %d", &N, &W, &H);
  for (int y=0; y<H; y++) {
    for (int x=0; x<W; x++) {
      char m;
      scanf(" %c", &m);
      grid[x][y] = m;
      if (ctoi(m) > 0) {
        initial_position[ctoi(m)] = make_pair(x, y);
      }
    }
  }

  
  //pair<int, int> ret = ending_place(4, 4, 1, 0);
  //printf("%d %d", ret.first, ret.second);

  for (int i=1; i<=N; i++) {
    bfs(i);
  }

  int depth=5;
  while (depth < 6) {
    printf("considering depth %d\n", depth);
    vector<vector<int> > partitions = unordered_partitions(depth, N);

    for (int i=0; i<partitions.size(); i++) { //consider all partitions
      vector<int> my_partition = partitions[i];
      printf("considering partition ");
      for (int j=0; j<my_partition.size(); j++) {
        printf("%d ", my_partition[j]);
      }
      printf("\n");

      vector<pair<int, int> > reachables[MAX_N];
      for (int robot_id=0; robot_id<=N; robot_id++) { //populate reachables
        int depth = partitions[i][robot_id - 1];
        for (map<pair<int, int>, int>::iterator l = dist[robot_id].begin(); l != dist[robot_id].end(); l++) {
          if (l->second == depth) {
            reachables[robot_id].push_back(l->first);
          }
        }
        sort(reachables[robot_id].begin(), reachables[robot_id].end());
      }

      /*
      vector<pair<int, int> > all_reachables = reachables[1];
      for (int robot_id=2; robot_id <= N; robot_id++) {
        printf("%d", partitions[i][robot_id - 1]);
        for (int k=0; k<all_reachables.size(); k++) {
          printf("(%d %d) ", all_reachables[k].first, all_reachables[k].second);
        }
        printf("\n");
        vector<pair<int, int> > new_all_reachables;
        set_intersection(all_reachables.begin(), all_reachables.end(), reachables[robot_id].begin(), reachables[robot_id].end(), inserter(new_all_reachables, new_all_reachables.begin()));
        all_reachables = new_all_reachables;
      }
      printf("got %d intersections\n", all_reachables.size());
      */
    }  

    depth++;
  }

  return 0;
}
