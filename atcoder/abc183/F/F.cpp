#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 200009;

int rep[MAX_N];
map<int, int> colours[MAX_N];
set<int> students[MAX_N];

int N, Q;

int main() {

  cin >> N >> Q;
  for (int i=0; i<N; i++) {
    rep[i] = i;
    int c;
    cin >> c;
    colours[i][c] = 1;
    students[i].insert(i);
  }

  while (Q--) {
    int t;
    cin >> t;
    if (t == 1) {
      int a, b;
      cin >> a >> b;
      a--; b--;
      a = rep[a]; b = rep[b];
      if (a == b) continue;
      if (students[a].size() < students[b].size()) {
        int tmp;
        tmp = a; a = b; b = tmp;
      }
      // merge B into A
      students[a].insert(students[b].begin(), students[b].end());
      for (auto const& [k, v] : colours[b]) {
        colours[a][k] += v;
      }
      for (const auto s : students[b]) rep[s] = a;
    } else {
      int x, y;
      cin >> x >> y;
      x--;
      x = rep[x];
      cout << colours[x][y] << endl;
    }
  }

  return 0;
}
