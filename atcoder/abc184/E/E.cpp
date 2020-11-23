#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

int H, W;
char grid[2009][2009];
bool visited[2009][2009];
bool visited_alphabet[29];
vector<pair<int, int>> loc_of_alpha[29];

vector<pair<int,int>> DELTA_DIR = {{0,1}, {0,-1}, {1,0}, {-1,0}};

int ans() {
  vector<pair<int, int>> frontier;
  for (int x=0; x<H; x++) {
    for (int y=0; y<W; y++) {
      if (grid[x][y] == 'S') {
        frontier = {{x, y}};
        visited[x][y] = true;
      }
    }
  }

  for (int i=0; i<26; i++) {
    loc_of_alpha[i] = vector<pair<int,int>>();
  }

  for (int x=0; x<H; x++) {
    for (int y=0; y<W; y++) {
      if ('a' <= grid[x][y] && grid[x][y] <= 'z') {
        loc_of_alpha[grid[x][y] - 'a'].push_back({x, y});
      }
    }
  }

  int ret = 1;

  while (1) {
    // cout << "ret=" << ret << "frontier=" << frontier << endl;
    vector<pair<int, int>> next_frontier;
    for (const auto p : frontier) {
      int x = p.first;
      int y = p.second;
      for (const auto p2 : DELTA_DIR) {
        int new_x = x + p2.first;
        int new_y = y + p2.second;

        if (!((0 <= new_x) && (new_x < H))) continue;
        if (!((0 <= new_y) && (new_y < W))) continue;
        if (visited[new_x][new_y]) continue;

        if (grid[new_x][new_y] == '#') continue;
        if (grid[new_x][new_y] == 'G') {
            // cout << "new_x=" << new_x << "new_y=" << new_y << endl;
          return ret;
        }

        visited[new_x][new_y] = true;
        next_frontier.push_back({new_x, new_y});


      }

      char c = grid[x][y];
      if ('a' <= c && c <= 'z' && !(visited_alphabet[c - 'a'])) {
        visited_alphabet[c - 'a'] = true;

        for (auto p3 : loc_of_alpha[c - 'a']) {
          if (visited[p3.first][p3.second]) continue;
          visited[p3.first][p3.second] = true;
          next_frontier.push_back({p3.first, p3.second});
        }

      }
    }
    frontier = next_frontier;
    ret += 1;
    if (frontier.size() == 0) return -1;
  }
}

int main() {

  cin >> H >> W;

  // cout << "H=" << H << "W=" << W << endl;

  for (int i=0; i<H; i++) {
    for (int j=0; j<W; j++) {
      visited[i][j] = false;
      cin >> grid[i][j];
      // cout << i << j << grid[i][j] << endl;
    }
  }

  for (int i=0; i<29; i++) {
    visited_alphabet[i] = false;
  }

  cout << ans() << endl;

  return 0;
}
