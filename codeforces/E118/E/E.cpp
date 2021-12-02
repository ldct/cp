#include <bits/stdc++.h>
using namespace std;

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

const vector<pair<int, int>> DIRECTIONS =  { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };


bool good(vector<vector<char>>& grid, int x, int y) {
  int R = grid.size();
  int C = grid[0].size();

  int need_to_block = 0;
  for (int z=0; z<4; z++) {
    auto p = DIRECTIONS[z];
    int new_x = x + p.first;
    int new_y = y + p.second;

    if (!((0 <= new_x) && (new_x < R))) continue;
    if (!((0 <= new_y) && (new_y < C))) continue;

    if (grid[new_x][new_y] == '.') need_to_block += 1;
  }
  return need_to_block <= 1;
}

void ans(vector<vector<char>>& grid) {
  int R = grid.size();
  int C = grid[0].size();

  vector<vector<bool>> visited;

  for (int i=0; i<R; i++) {
    visited.push_back(vector<bool>(C, false));
  }

  int px, py;

  stack<pair<int, int>> worklist;

  // initial scan
  for (int i=0; i<R; i++) for (int j=0; j<C; j++) {
    if (grid[i][j] == 'L') {
      px = i; py = j;
    }
    if (grid[i][j] == '+') {
      for (int z=0; z<4; z++) {
        auto p = DIRECTIONS[z];
        int new_x = i + p.first;
        int new_y = j + p.second;

        if (!((0 <= new_x) && (new_x < R))) continue;
        if (!((0 <= new_y) && (new_y < C))) continue;
        if (grid[new_x][new_y] == '.') {
          // cout << make_pair(new_x, new_y) << endl;
          worklist.push({new_x, new_y});
        }

      }
    }
  }

  // neighbours of p
  for (int z=0; z<4; z++) {
    auto p = DIRECTIONS[z];
    int new_x = px + p.first;
    int new_y = py + p.second;

    if (!((0 <= new_x) && (new_x < R))) continue;
    if (!((0 <= new_y) && (new_y < C))) continue;
    if (grid[new_x][new_y] == '.') worklist.push({new_x, new_y});
  }

  while (worklist.size()) {
    auto p = worklist.top();
    int x = p.first;
    int y = p.second;
    worklist.pop();
    if (visited[x][y]) continue;
    visited[x][y] = true;

    if (good(grid, x, y)) {
      grid[x][y] = '+';

      for (int z=0; z<4; z++) {
        auto p = DIRECTIONS[z];

        int new_x = x + p.first;
        int new_y = y + p.second;

        if (
          (0 <= new_x) &&
          (new_x < R) &&
          (0 <= new_y) &&
          (new_y < C) &&
          grid[new_x][new_y] == '.'
        ) {
          visited[new_x][new_y] = false;
          if (!visited[new_x][new_y]) worklist.push({new_x, new_y});
        }
      }

    }
  }
}

int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int T;
  cin >> T;
  while (T --> 0) {
    int N, M;
    cin >> N >> M;
    vector<vector<char>> grid;
    for (int i=0; i<N; i++) {
      vector<char> row;
      for (int j=0; j<M; j++) {
        char c;
        cin >> c;
        row.push_back(c);
      }
      grid.push_back(row);
    }
    ans(grid);

    for (int i=0; i<N; i++) {
      string S = "";
      for (int j=0; j<M; j++) {
        S += grid[i][j];
      }
      cout << S << '\n';
    }
  }

  return 0;
}
