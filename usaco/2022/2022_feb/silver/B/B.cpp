#include <bits/stdc++.h>
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

struct pair_hash {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1,T2> &p) const {
        auto h1 = std::hash<T1>{}(p.first);
        auto h2 = std::hash<T2>{}(p.second);

        // Mainly for demonstration purposes, i.e. works but is overly simple
        // In the real world, use sth. like boost.hash_combine
        return h1*239 + h2;
    }
};

int N, n, xg, yg;
vector<pair<int, int>> instructions1, instructions2;
unordered_map<pair<int, int>, vector<int>, pair_hash> achievable;
vector<int> ret;

void bump(vector<int>& lst, int l) {
  for (int i=0; i<lst.size(); i++) {
    if (i + l < N+1) {
      ret[i+l] += lst[i];
    }
  }
}

pair<int, int> total(int mask, vector<pair<int, int>>& vec) {
  int x = 0;
  int y = 0;
  for (int i=0; i<vec.size(); i++) {
    if (mask & (1 << i)) {
      x += vec[i].first;
      y += vec[i].second;
    }
  }
  return {x, y};
}

i32 main() {

  cin >> N >> xg >> yg;
  ret = vector<int>(N+1, 0);
  n = N / 2;

  for (int i=0; i<n; i++) {
    int x, y;
    cin >> x >> y;
    instructions1.push_back({x, y});
  }
  for (int i=0; i<N-n; i++) {
    int x, y;
    cin >> x >> y;
    instructions2.push_back({x, y});
  }

  for (uint32_t i=0; i<(1<<instructions1.size()); i++) {
    auto t = total(i, instructions1);
    if (!achievable.count(t)) {
      achievable[t] = vector<int>(instructions1.size()+1, 0);
    }
    achievable[t][__builtin_popcount(i)] += 1;
  }

  for (uint32_t i=0; i<(1<<instructions2.size()); i++) {
    auto t = total(i, instructions2);

    int x = xg - t.first;
    int y = yg - t.second;

    pair<int, int> p = {x, y};

    if (achievable.count(p)) {
        bump(achievable[p], __builtin_popcount(i));
    }
  }

  for (int i=1; i<=N; i++) {
    cout << ret[i] << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS