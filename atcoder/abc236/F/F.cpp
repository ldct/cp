#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

int basis[32]; // basis[i] keeps the mask of the vector whose f value is i

int sz; // Current size of the basis

int N;

bool insertVector(int mask) {
	for (int i = 0; i < N; i++) {
		if ((mask & 1 << i) == 0) continue; // continue if i != f(mask)

		if (!basis[i]) { // If there is no basis vector with the i'th bit set, then insert this vector into the basis
			basis[i] = mask;
			++sz;

			return true;
		}

		mask ^= basis[i]; // Otherwise subtract the basis vector from this vector
	}
  return false;
}

i32 main() {

  cin >> N;

  vector<pair<int, int>> spices;

  for (int i=0; i<((1 << N) - 1); i++) {
    int c;
    cin >> c;
    spices.push_back({c, i+1});
  }

  sort(spices.begin(), spices.end());

  int ret = 0;
  for (auto [c, i] : spices) {
    bool res = insertVector(i);
    if (res) ret += c;
    // cout << "c=" << c << "i=" << i << "res=" << res << endl;
  }

  cout << ret << endl;
  // cout << spices << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS