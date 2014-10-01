#include <cstdio>
#include <vector>
#include <queue>
#include <iostream>
#include <set>

using namespace std;

typedef vector<vector<char> > grid;

char flip_c(char c) {
  if (c == '*') {
    return '.';
  } else {
    return '*';
  }
}

vector<vector<char> > flip(vector<vector<char> > grid, int x, int y) {
  vector<vector<char> > ret = vector<vector<char> >(grid);

  ret[x][y] = flip_c(grid[x][y]);

  if (x < 2) {
    ret[x+1][y] = flip_c(grid[x+1][y]);
  }
  if (y < 2) {
    ret[x][y+1] = flip_c(grid[x][y+1]);
  }
  if (0 < x) {
    ret[x-1][y] = flip_c(grid[x-1][y]);
  }
  if (0 < y) {
    ret[x][y-1] = flip_c(grid[x][y-1]);
  }
  return ret;
}

bool all_white(vector<vector<char> > grid) {
  for (int i=0; i<3; i++) {
    for (int j=0; j<3; j++) {
      if (grid[i][j] == '*') {
        return false;
      }
    }
  }
  return true;
}

int main() {

  int P;
  char s;

  scanf("%d\n", &P);

  while (P--) {

    vector<vector<char> > target;
    priority_queue<pair<int, vector<vector<char> > > > q;
    set<vector<vector<char> > > seen;

    for (int i=0; i<3; i++) {
      vector<char> row;
      for (int j=0; j<3; j++) {
        scanf("%c", &s);
        row.push_back(s);
      }
      target.push_back(row);
      scanf("\n");
    }

    q.push(make_pair(0, target));

    while (1) {
      pair<int, vector<vector<char> > > curr = q.top();
      q.pop();

      if (seen.count(curr.second) > 0) {
        continue;
      }

      seen.insert(curr.second);

      int layer = -curr.first;

      if (all_white(curr.second)) {
        cout << layer << endl;
        break;
      }

      for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
          q.push(make_pair(-(layer + 1), flip(curr.second, i, j)));
        }
      }
    }

  }

  return 0;
}
