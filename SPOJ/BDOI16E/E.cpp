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

#define int long long

int N;
vector<int> children [100009];
long long joy[100009];
long long joy_delta[100009];
long long ret[100009];

typedef struct _VeniceSet {
	set<long long> S;
	long long water_level = 0;
	void add(long long v) {
		S.insert(v - water_level);
	}
	void remove(long long v) {
		S.erase(S.find(v + water_level));
	}
	void updateAll(long long v) {
		water_level += v;
	}
	int size() {
		return S.size();
	}
  set<long long> asSet() {
    set<long long> ret;
    for (const auto s : S) {
      ret.insert(s + water_level);
    }
    return ret;
  }
  void merge(struct _VeniceSet& other) {
    for (const auto s : other.asSet()) {
      add(s);
    }
  }
} VeniceSet;

VeniceSet elems[100009];

void dfs(int u) {
  for (const auto v : children[u]) {
    dfs(v);
  }

  for (const auto v : children[u]) {
    elems[v].updateAll(joy_delta[v]);
  }

  if (u < 0) {
    cout << "before swap" << endl;
    cout << elems[u].asSet();
    for (const auto v : children[u]) cout<< elems[v].asSet();
    cout << endl;
  }

  for (const auto v : children[u]) {
    if (elems[v].size() > elems[u].size()) {
      swap(elems[u], elems[v]);
    }
  }

  if (u < 0) {
    cout << "after swap" << endl;
    cout << elems[u].asSet();
    for (const auto v : children[u]) cout<< elems[v].asSet();
    cout << endl;
  }

  for (const auto v : children[u]) {
    elems[u].merge(elems[v]);
  }

  if (u < 0) {
    cout << "after merge" << endl;
    cout << elems[u].asSet();
    for (const auto v : children[u]) cout<< elems[v].asSet();
    cout << endl;
  }

  ret[u] = elems[u].S.size();
  // cout << "u=" << u << "ans=" << elems[u].asSet() << endl;
}

int grand_house = -1;

int32_t main() {

  cin >> N;
  for (int i=0; i<N; i++) { cin >> joy[i]; }
  for (int i=0; i<N; i++) {
    int v;
    cin >> v;
    if (v == 0) {
      grand_house = i;
      continue;
    };
    v--;
    children[v].push_back(i);
  }
  for (int i=0; i<N; i++) { cin >> joy_delta[i]; }

  for (int i=0; i<N; i++) {
    elems[i].add(joy[i]);
  }

  dfs(grand_house);

  for (int i=0; i<N; i++) { cout << ret[i] << endl; }

  return 0;
}
