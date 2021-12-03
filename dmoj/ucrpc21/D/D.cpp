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

int r, c, R, C;
char grid[2009][2009];
int colour[2009][2009];

void dfs(int i, int j, int c) {
  if (!(0 <= i && i < R)) return;
  if (!(0 <= j && j < C)) return;
  if (colour[i][j] != -1) return;
  if (grid[i][j] != '.') return;
  colour[i][j] = c;
  dfs(i+1, j, c);
  dfs(i-1, j, c);
  dfs(i, j+1, c);
  dfs(i, j-1, c);
}

int main() {

  memset(colour, -1, sizeof(colour));

  cin >> r >> c;
  R = 2*r+1;
  C = 2*c+1;

  for (int i=0; i<R; i++) {
    for (int j=0; j<C; j++) {
      cin >> grid[i][j];
    }
  }

  int c = 0;
  for (int i=0; i<R; i++) {
    for (int j=0; j<C; j++) {
      if (grid[i][j] == '.' && colour[i][j] == -1) {
        dfs(i, j, c);
        c++;
      }
    }
  }

  // for (int i=0; i<R; i++) {
  //   for (int j=0; j<C; j++) {
  //     cout << grid[i][j];
  //   }
  //   cout << endl;
  // }

  // for (int i=0; i<R; i++) {
  //   for (int j=0; j<C; j++) {
  //     if (colour[i][j] == -1) {
  //       cout << ' ';
  //     } else {
  //       cout << colour[i][j];
  //     }
  //   }
  //   cout << endl;
  // }

  map<int, int> freq;

  for (int i=0; i<R; i++) {
    for (int j=0; j<C; j++) {
      if ((i % 2) == 1 && (j % 2) == 1) freq[colour[i][j]]++;
    }
  }

  vector<int> ret;
  for (int i=0; i<c; i++) {
    ret.push_back(freq[i]);
  }

  sort(ret.begin(), ret.end());
  reverse(ret.begin(), ret.end());

  for (auto r : ret) {
    cout << r << " ";
  }
  cout << endl;

  return 0;
}
