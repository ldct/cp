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

int MAX_DIGITS = 10;

vector<int> digits(int num) {
  vector<int> ret;
  while(num!=0){
      int temp = num%10;
      ret.push_back(temp);
      num /= 10;
  }

  while (ret.size() < MAX_DIGITS) ret.push_back(0);
  reverse(ret.begin(), ret.end());
  return ret;
}

int int_pow(int b, int e) {
  if (e == 0) return 1;
  return b*int_pow(b, e-1);
}

int count(int n) {
  int ret = 0;

  auto x = digits(n);

  for (int i=0; i<x.size(); i++) {
    for (int j=0; j<x[i]; j++) {
      int d = x.size()-i-1;
      int d10 = int_pow(10, d);
      int s = 0;

      for (int k=0; k<i; k++) s += x[k];
      s += j;

      int r = s*d10 + 9*d*d10/2;

      ret += r;
    }
  }

  return ret;


}

int ans(int a, int b) {
  return count(b+1) - count(a);
}

// while True:
//     a, b = read_int_tuple()
//     if (a, b) == (-1, -1):
//         break
//     print(ans(a, b))

i32 main() {

  while (1) {
    int a, b;
    cin >> a >> b;
    if (a == -1 && b == -1) return 0;
    cout << ans(a, b) << endl;
  }
  return 0;
}
