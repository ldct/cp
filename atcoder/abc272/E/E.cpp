#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>
#include <unordered_map>
#include <cassert>

using namespace std;
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

int val(vector<int>& A, int i, int m) {
  return A[i] + (i+1)*(m+1);
}

int mex(vector<int>& A) {
  if (A.size() == 0) return 0;
  int M = 0;
  for (auto a : A) {
    M = max(a, M);
  }
  auto sA = set<int>(A.begin(), A.end());
  for (int i=0; i<=M+1; i++) {
    if (sA.count(i) == 0) return i;
  }
  return 0;
  // assert(false); return 0;
}

int N, M;
vector<int> A;
vector<int> entries[200009];

i32 main() {

  cin.tie(0);

  cin >> N >> M;
  A = vector<int>(N, 0);

  for (int i=0; i<N; i++) {
    cin >> A[i];
  }

  for (int i=0; i<A.size(); i++) {
    int entry_time = max(0LL, (-A[i] / (i+1)) - 2);
    // cout << "entry_time=" << entry_time << endl;
    if (entry_time <= M+1) {
      entries[entry_time].push_back(i);
    }
  }

  vector<int> ret;
  set<int> active_indexes;

  for (int m=0; m<M; m++) {
    for (auto idx : entries[m]) {
      active_indexes.insert(idx);
    }

    auto ei2 = set<int>(active_indexes);

    for (auto idx : ei2) {
      if (val(A, idx, m) > N) {
        active_indexes.erase(active_indexes.find(idx));
      }
    }

    vector<int> active_values;

    for (auto i : active_indexes) {
      active_values.push_back(val(A, i, m));
    }

    // cout << m << active_indexes << endl;

    ret.push_back(mex(active_values));
  }

  for (auto r : ret) {
    cout << r << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS