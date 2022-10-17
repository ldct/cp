#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>
#include <unordered_map>

using namespace std;
#define int long long
#define i32 int32_t
#define i64 int64_t

namespace io_aux {
    namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
  
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
} using namespace io_aux;

int N, X;

int TARGET = 0;
int ORIGIN = 1;
int WALL = 2;
int KEY = 3;

int Y[2000];
int Z[2000];

vector<tuple<int, int, int>> items;

int pos(tuple<int,int,int>& item){ return get<0>(item); }

int kind(tuple<int,int,int>& item){ return get<1>(item); }

int sig(tuple<int,int,int>& item){ return get<2>(item); }

int dist(int x, int y) {
  // cout << items.size();
  // cout << "dist " << x << " " << y << endl;
  int r = pos(items[x]) - pos(items[y]);
  return r < 0 ? -r : r;
}

int idx_of_key[2000];

int add(int a, int b) {
  if (b == LLONG_MAX) return LLONG_MAX;
  return a + b;
}

int memo[3009][3009][2];

int ans(int a, int b, bool is_left) {

  if (memo[a][b][is_left] != -1) return memo[a][b][is_left];

  auto curr_pos = b;
  if (is_left) curr_pos = a;

  if (kind(items[curr_pos]) == TARGET) return memo[a][b][is_left] = 0;

  int ret = LLONG_MAX;

  int aa = a-1;
  if (aa >= 0) {
    auto& item = items[aa];
    auto cost = dist(curr_pos, aa);
    bool ok = true;

    if (kind(item) == WALL && !(a <= idx_of_key[sig(item)] && idx_of_key[sig(item)] <= b)) {
      ok = false;
    }
    if (ok) {
      ret = min(ret, add(cost, ans(aa, b, true)));
    }
  }

  int bb=b+1;
  if (bb < items.size()) {
    auto& item = items[bb];
    auto cost = dist(curr_pos, bb);
    bool ok = true;

    if (kind(item) == WALL && !(a <= idx_of_key[sig(item)] && idx_of_key[sig(item)] <= b)) {
      ok = false;
    }
    if (ok) {
      ret = min(ret, add(cost, ans(a, bb, false)));
    }
  }

  return memo[a][b][is_left] = ret;
}

i32 main() {

  memset(memo, -1, sizeof(memo));

  cin.tie(0);

  cin >> N >> X;
  for (int i=0; i<N; i++) {
    cin >> Y[i];
  }
  for (int i=0; i<N; i++) {
    cin >> Z[i];
  }

  items.push_back({X, TARGET, -1});
  items.push_back({0, ORIGIN, -1});

  for (int i=0; i<N; i++) {
    items.push_back({Y[i], WALL, i});
  }

  for (int i=0; i<N; i++) {
    items.push_back({Z[i], KEY, i});
  }

  sort(items.begin(), items.end());

  for (int i=0; i<items.size(); i++) {
    auto& item = items[i];
    if (kind(item) == KEY) {
      idx_of_key[sig(item)] = i;
    }
  }

  int i=0;
  for (i=0; i<items.size(); i++) {
    if (ORIGIN == kind(items[i])) {
      break;
    }
  }


  // cout << "items=" << items << endl;
  // cout << "origin i=" << i << endl;
  auto r = ans(i,i,true);
  if (r == LLONG_MAX) {
    r = -1;
  }

  cout << r << endl;

}

// DO NOT USE FOR INTERACTIVE PROBLEMS