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

using ll = long long;
using db = long double; // or double, if TL is tight
using pi = pair<int,int>;
using pl = pair<ll,ll>;
using pd = pair<db,db>;
using vi = vector<int>;
using vb = vector<bool>;
using vl = vector<ll>;
#define sz(x) int((x).size())
#define bg(x) begin(x)
#define all(x) bg(x), end(x)
#define pb push_back
// loops
#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define F0R(i,a) FOR(i,0,a)
#define ROF(i,a,b) for (int i = (b)-1; i >= (a); --i)
#define R0F(i,a) ROF(i,0,a)
#define rep(a) F0R(_,a)
#define each(a,x) for (auto& a: x)


vi sa_is(const vi& s, int upper) {
  int n = sz(s); if (!n) return {};
  vi sa(n); vb ls(n); /// is suffix starting at i < suffix starting at i+1
  R0F(i,n-1) ls[i] = s[i] == s[i+1] ? ls[i+1] : s[i] < s[i+1]; 
  /// s-type: less than next suffix -> ls[i] = 1 
  /// l-type: greater than next suffix -> ls[i] = 0
  vi sum_l(upper), sum_s(upper);
  F0R(i,n) (ls[i] ? sum_l[s[i]+1] : sum_s[s[i]])++; /// note that s[i] = upper-1 -> !ls[i]
  F0R(i,upper) { 
    if (i) sum_l[i] += sum_s[i-1]; /// sum_l[i] = sum_{j=0}^{i-1}(s_j+l_j)
    sum_s[i] += sum_l[i]; /// sum_s[i] = sum_{j=0}^{i-1}s_j+sum_{j=0}^{i}l_j
  }
  auto induce = [&](const vi& lms) {
    fill(all(sa),-1);
    vi buf = sum_s;
    for (int d: lms) if (d != n) sa[buf[s[d]]++] = d; /// lms is s-type, first few ...
    buf = sum_l; sa[buf[s[n-1]]++] = n-1;
    F0R(i,n) { /// do l-type in increasing order, suf[v] > suf[v+1]
      int v = sa[i]-1;
      if (v >= 0 && !ls[v]) sa[buf[s[v]]++] = v;
    }
    buf = sum_l;
    R0F(i,n) { /// do s-type in decreasing order, suf[v] < suf[v+1]
      int v = sa[i]-1;
      if (v >= 0 && ls[v]) sa[--buf[s[v]+1]] = v; /// lms is s-type, last few ...
    }
  };
  vi lms_map(n+1,-1), lms; int m = 0;
  FOR(i,1,n) if (!ls[i-1] && ls[i]) lms_map[i]=m++, lms.pb(i);
  induce(lms); // sorts LMS prefixes
  vi sorted_lms;each(v,sa)if (lms_map[v]!=-1)sorted_lms.pb(v);
  vi rec_s(m); int rec_upper = 0; // smaller subproblem
  FOR(i,1,m) { // compare two lms substrings in sorted order
    int l = sorted_lms[i-1], r = sorted_lms[i];
    int end_l = lms_map[l]+1 < m ? lms[lms_map[l]+1] : n;
    int end_r = lms_map[r]+1 < m ? lms[lms_map[r]+1] : n;
    bool same = 0; // whether lms substrings are same
    if (end_l-l == end_r-r) {
      for (;l < end_l && s[l] == s[r]; ++l,++r);
      if (l != n && s[l] == s[r]) same = 1;
    }
    rec_s[lms_map[sorted_lms[i]]] = (rec_upper += !same);
  }
  vi rec_sa = sa_is(rec_s,rec_upper+1);
  F0R(i,m) sorted_lms[i] = lms[rec_sa[i]];
  induce(sorted_lms); // sorts LMS suffixes
  return sa;
}

vector<int> suffix_array(string s) {
  vector<int> ss;
  for (auto c : s) {
    if (c == '$') {
      ss.push_back(0);
    } else if (c == '~') {
      ss.push_back(27);
    } else if ('a' <= c && c <= 'z'){
      ss.push_back(c - 'a' + 1);
    } else {
      cout << "c=" << c << endl;
      assert(false);
    }
  }
  return sa_is(ss, 28);
}

vector<int> relative_order(string s) {
  auto sa = suffix_array(s);
  vector<pair<int, int>> ps;
  for (int i=0; i<sa.size(); i++) {
    ps.push_back({sa[i], i});
  }
  sort(ps.begin(), ps.end());
  vector<int> ret;
  for (auto p : ps) {
    ret.push_back(p.second);
  }
  return ret;
}

string S;

i32 main() {

  cin >> S;
  int N = S.size();

  auto ro = relative_order(S+S);

  int min_score = INT_MAX;

  for (int i=0; i<N; i++) {
    min_score = min(min_score, ro[i]);
  }

  int argmin = 0;
  for (int i=0; i<N; i++) {
    if (ro[i] == min_score) {
      argmin = i;
    }
  }

  int idx = argmin;

  string ret;

  for (int i=0; i<N; i++) {
    int j = (i + idx) % N;
    char c = S[j];
    ret.push_back(c);
  }

  cout << ret << endl;

  return 0;
}