#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>

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

int N;
vector<int> A;
vector<int> ri;

int memo[200009];

int matchings(int i) {
  if (i >= A.size()) return 0;
  if (memo[i] != -1) return memo[i];
  int j = ri[i];
  if (j == -1) return memo[i] = matchings(i+1);
  return memo[i] = max(
    matchings(i+1),
    1+matchings(j)
  );
}

int ans() {

  for (int i=0; i<=N; i++) {
    memo[i] = -1;
  }
  
  vector<int> B;
  B.push_back(0);
  for (auto a : A) {
    B.push_back(B[B.size()-1]^a);
  }

  ri = vector<int>(B.size(), -1);

  map<int, int> m;
  for (int i=B.size()-1; i!=-1; i--) {
    auto b = B[i];
    if (m.count(b) > 0) {
      ri[i] = m[b];
    }
    m[b] = i;
  }

  // cout << B << endl;
  // cout << ri << endl;
  // cout << matchings(0) << endl;

  return A.size() - matchings(0);
}

i32 main() {

  int T;
  cin >> T;

  while (T --> 0) {
    A.clear();
    cin >> N;

    for (int i=0; i<N; i++) {
      int a; cin >> a; A.push_back(a);
    }

    // cout << A << endl;
    cout << ans() << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS