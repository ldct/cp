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

int u, v, p;

int modinv(int a, int b) {
	int b0 = b, t, q;
	int x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}

int move(int u, int p, int r) {
  if (r == 0) {
    u++;
  } else if (r == 1) {
    u--;
  } else {
    u = modinv(u, p);
  }
  u += p;
  u %= p;
  assert( 0 <= u );
  assert( u < p );
  return u;
}

bool verify(int u, int v, vector<int> moves) {
  for (auto r : moves) {
    u = move(u, p, r);
  }
  return u == v;
}

pair<int, vector<int>> random_seq(int u, int p) {
  int old_u = u;
  vector<int> moves;
  for (int i=0; i<100; i++) {
    int r = rand() % 3;
    if (u == 0) r = rand() % 2;
    moves.push_back(r);
    u = move(u, p, r);
  }
  return {u, moves};
}

int main() {

  cin >> u >> v >> p;
  unordered_map<int, vector<int>> u_end, v_end;
  for (int i=0; i<100009; i++) {
    auto r = random_seq(u, p);
    u_end[r.first] = r.second;
    r = random_seq(v, p);
    v_end[r.first] = r.second;
    assert(verify(v, r.first, r.second));
  }

  for (auto& [t, moves] : u_end) {
    if (v_end.count(t)) {
      // cout << "ok" << endl;

      assert(verify(u, t, moves));

      auto right_moves = v_end[t];

      assert(verify(v, t, right_moves));

      vector<int> new_right;
      for (auto r : right_moves) {
        if (r < 2) r = 1 - r;
        new_right.push_back(r);
      }
      reverse(new_right.begin(), new_right.end());

      // cout << "right_moves=" << right_moves << endl;
      // cout << "new_right=" << new_right << endl;

      auto s = t;
      vector<int> betweens;
      for (auto r : new_right) {
        s = move(s, p, r);
        betweens.push_back(s);
      }
      // cout << betweens << endl;
      assert(verify(t, v, new_right));

      for (auto r : new_right) moves.push_back(r);

      assert(verify(u, v, moves));

      cout << moves.size() << endl;
      for (auto r : moves) {
        cout << (r+1) << endl;
      }

      return 0;
    }
  }
  return 0;
}
