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

int CeilIndex(vector<pair<int, int>>& v, int l, int r, pair<int,int> key) {
    while (r - l > 1) {
        int m = l + (r - l) / 2;
        if (v[m] >= key)
            r = m;
        else
            l = m;
    }

    return r;
}

vector<int> LIS(vector<pair<int,int>>& v) {
    vector<pair<int,int>> tail(v.size());
    vector<int> ts(v.size(), 0);
    vector<int> ret;
    int length = 1; // always points empty slot in tail

    tail[0] = v[0];
    ts[0] = 1;
    ret.push_back(1);

    for (size_t i = 1; i < v.size(); i++) {

      // cout << "A[" << i << "]=" << v[i] << " ";

        // new smallest value
        if (v[i] < tail[0]) {
          // cout << "case 1" << endl;
          tail[0] = v[i];
          ret.push_back(ts[0]);
        }

        // v[i] extends largest subsequence
        else if (v[i] >= tail[length - 1]) {
          // cout << "case 2" << endl;
          tail[length] = v[i];
          ts[length] = ts[length-1] + 1;
          ret.push_back(ts[length]);
          length++;
        }

        else {
          // cout << "case 3" << endl;
          int j = CeilIndex(tail, -1, length, v[i]);
          tail[j] = v[i];
          ret.push_back(ts[j]);
        }
    }

    return ret;
}

vector<int> ans(vector<int> v) {
  vector<pair<int,int>> vv;
  for (int i=0; i<v.size(); i++) {
    vv.push_back(make_pair(v[i], i));
  }
  return LIS(vv);
}

int main()
{
    vector<int> v{1, 2, 3, 2};
    cout << ans(v) << endl;
    v = {2, 2, 1};
    cout << ans(v) << endl;
    v = {3,1,5,6,4,2};
    cout << ans(v) << endl;
    return 0;
}
