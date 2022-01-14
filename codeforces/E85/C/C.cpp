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

int T, N;
vector<int> A, B;

int ans() {
  int ret = 0;
  for (int i=0; i<N; i++) {
    int j = (i+1) % N;
    int new_val = min(B[i], A[j]);
    ret += (A[j] - new_val);
    A[j] = new_val;
  }
  return *(min_element(A.begin(), A.end())) + ret;
}

i32 main() {

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> T;
  while (T --> 0) {
    A.clear(); B.clear();
    cin >> N;
    for (int i=0; i<N; i++) {
      int a, b;
      cin >> a >> b;
      A.push_back(a); B.push_back(b);
    }
    // cout << A << B << endl;
    cout << ans() << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS