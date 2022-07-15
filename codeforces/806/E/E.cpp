#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

struct UF {
  vector<int> e;
  UF(int n) : e(n, -1) {}
  bool sameSet(int a, int b) { return find(a) == find(b); }
  int size(int x) { return -e[find(x)]; }
  int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
  bool join(int a, int b) {
    a = find(a), b = find(b);
    if (a == b) return false;
    if (e[a] > e[b]) swap(a, b);
    e[a] += e[b]; e[b] = a;
    return true;
  }
};

int N;
vector<string> grid;

void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int a = 0;
        int b = n-1;
        while(a<b){
            for(int i=0;i<(b-a);++i){
                swap(matrix[a][a+i], matrix[a+i][b]);
                swap(matrix[a][a+i], matrix[b][b-i]);
                swap(matrix[a][a+i], matrix[b-i][a]);
            }
            ++a;
            --b;
        }
    }

int score(vector<int>& v) {
  int s = 0;
  for (auto e : v) {
    s += e;
  }
  return min(
    s, (int)v.size() - s
  );
}
int solve() {
  int k=0;
  vector<vector<int>> grid3;
  for (int i=0; i<N; i++) {
    vector<int> row;
    for (int j=0; j<N; j++) {
      row.push_back(k);
      k++;
    }
    grid3.push_back(row);
  }

  auto g = UF(N*N);

  k = 0;
  vector<vector<int>> grid2;
  for (int i=0; i<N; i++) {
    vector<int> row;
    for (int j=0; j<N; j++) {
      row.push_back(k);
      k++;
    }
    grid2.push_back(row);
  }
  for (int z=0; z<4; z++) {
    rotate(grid2);

    for (int i=0; i<N; i++) for (int j=0; j<N; j++) {
      g.join(
        grid3[i][j],
        grid2[i][j]
      );
    }
  }

  vector<vector<int>> elems;

  for (int t=0; t<N*N; t++) {
    elems.push_back(vector<int>());
  }

  for (int i=0; i<N; i++) for (int j=0; j<N; j++) {
    auto p = g.find(grid3[i][j]);
    elems[p].push_back(grid[i][j] == '0' ? 0 : 1);
  }

  // cout << elems << endl;

  int ret = 0;

  for (int k = 0; k < elems.size(); k++) {
    ret += score(elems[k]);
  }
  return ret;
}

i32 main() {

  int T;
  cin >> T;
  while (T --> 0) {
    cin >> N;
    grid.clear();
    for (int i=0; i<N; i++) {
      string s;
      cin >> s;
      grid.push_back(s);
    }
    cout << solve() << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS