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

vector<bool> ss_ncp(int target, vector<int> B) {
  auto possible = vector<bool>(target+1, false);
  possible[0] = true;

  for (auto b : B) {
    for (int mass=target; mass!=-1; mass--) {
      // cout << "test " << b << " " << mass << endl;
      if (possible[mass] && (mass + b <= target))
          possible[mass+b] = true;
      }
  } 

  return possible;
}

int N, K;
vector<int> A;

bool ok(int i) {
  if (i >= N) return false;

  auto T = K;
  auto x = A[i];
  auto B = vector<int>(A);
  B.erase(B.begin() + i);
  // cout << "B=" << B << endl;
  auto p = ss_ncp(T, B);
  // cout << "p=" << p << endl;
  auto good = false;
  for (int w=0; w<p.size(); w++) {
    if (!p[w]) continue;
    if (w < K && K <= w+x) {
      good = true;
    }
  }
  return !good;
}


i32 main() {

  cin >> N >> K;
  A = vector<int>(N, 0);
  for (int i=0; i<N; i++) {
    cin >> A[i];
  }

  for (int i=0; i<N; i++) {
    A[i] = min(A[i], K+1);
  }

  sort(A.begin(), A.end());
  // cout << A << endl;

  int low = 0; int high = A.size();
  if (!ok(low)) {
    cout << 0 << endl; return 0;
  }

  for (int i=0; i<A.size(); i++) {
    // cout << i << " " << ok(i) << endl;
  }

  while (high - low > 2) {
    auto mid = (low + high) / 2;
    if (ok(mid)) {
      low = mid;
    } else {
      high = mid;
    }
  }

  while (ok(low)) low++;

  cout << low << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS