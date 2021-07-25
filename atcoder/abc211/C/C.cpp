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

vector<int> elems;

int memo[100009][10];
constexpr int MODULUS = 1000000007;

int ans(int i, int next) {
  if (i == elems.size()) {
    if (next == 8) return 1;
    return 0;
  }
  if (memo[i][next] != -1) return memo[i][next];

  if (next == elems[i]) {
    return memo[i][next] = (ans(i+1, next) + ans(i+1, next+1)) % MODULUS;
  }
  return ans(i+1, next);
}

int main() {

  string S;
  cin >> S;

  memset(memo, -1, sizeof(memo));

  for (char c : S) {
    if (c == 'c') elems.push_back(0);
    if (c == 'h') elems.push_back(1);
    if (c == 'o') elems.push_back(2);
    if (c == 'k') elems.push_back(3);
    if (c == 'u') elems.push_back(4);
    if (c == 'd') elems.push_back(5);
    if (c == 'a') elems.push_back(6);
    if (c == 'i') elems.push_back(7);
  }

  // cout << elems << endl;
  cout << ans(0, 0) << endl;
  return 0;
}
