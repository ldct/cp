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

template <class Tuple,
   class T = std::decay_t<std::tuple_element_t<0, std::decay_t<Tuple>>>>
std::vector<T> to_vector(Tuple&& tuple)
{
    return std::apply([](auto&&... elems){
        return std::vector<T>{std::forward<decltype(elems)>(elems)...};
    }, std::forward<Tuple>(tuple));
}

int M;
int p[10];
vector<int> neighbours[10];

bool is_end(tuple<int,int,int,int,int,int,int,int,int> state) {
  if (get<0>(state) != 0) return false;
  if (get<1>(state) != 1) return false;
  if (get<2>(state) != 2) return false;
  if (get<3>(state) != 3) return false;
  if (get<4>(state) != 4) return false;
  if (get<5>(state) != 5) return false;
  if (get<6>(state) != 6) return false;
  if (get<7>(state) != 7) return false;
  return true;
}

int get_idx(tuple<int,int,int,int,int,int,int,int,int> state, int target) {
  if (get<0>(state) == target) return 0;
  if (get<1>(state) == target) return 1;
  if (get<2>(state) == target) return 2;
  if (get<3>(state) == target) return 3;
  if (get<4>(state) == target) return 4;
  if (get<5>(state) == target) return 5;
  if (get<6>(state) == target) return 6;
  if (get<7>(state) == target) return 7;
  if (get<8>(state) == target) return 8;
  assert(-1);
  return -1;
}

tuple<int,int,int,int,int,int,int,int,int> swap_idx(tuple<int,int,int,int,int,int,int,int,int> state, int i, int j) {
  auto p = to_vector(state);
  swap(p[i], p[j]);
  return tuple<int,int,int,int,int,int,int,int,int>(
    p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8]
  );
}

map<tuple<int,int,int,int,int,int,int,int,int>, int> memo;

int ans(tuple<int,int,int,int,int,int,int,int,int> state) {
  if (is_end(state)) return 0;
  if (memo[state] != 0) return memo[state];
  int ret = 362881;
  int u = get_idx(state, 8);
  for (auto v : neighbours[u]) {
    // cout << "swapping" << u << v << endl;
    ret = min(ret, 1 + ans(swap_idx(state, u, v)));
  }
  return memo[state] = ret;
}

tuple<int,int,int,int,int,int,int,int,int> burnish(tuple<int,int,int,int,int,int,int,int> tup) {
  vector<int> arr = to_vector(tup);
  sort(arr.begin(), arr.end());
  int missing = -1;
  for (int i=0; i<100; i++) {
    if (arr[i] != i) {
      missing = i;
      break;
    }
  }
  return tuple<int,int,int,int,int,int,int,int,int>(
    p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],missing
  );
}

tuple<int,int,int,int,int,int,int,int,int> inv(tuple<int,int,int,int,int,int,int,int,int> tup) {

  auto arr = to_vector(tup);
  int arr2[arr.size()];


  for (int i = 0; i < arr.size(); i++)
    arr2[arr[i]] = i;


  return tuple<int,int,int,int,int,int,int,int,int>(
    arr2[0],arr2[1],arr2[2],arr2[3],arr2[4],arr2[5],arr2[6],arr2[7],arr2[8]
  );
}


int main() {

  cin >> M;
  for (int i=0; i<M; i++) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    neighbours[u].push_back(v);
    neighbours[v].push_back(u);
  }
  for (int i=0; i<8; i++) {
    cin >> p[i];
    p[i]--;
  }

  auto _start = tuple<int,int,int,int,int,int,int,int>(
    p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7]);

  auto start = inv(burnish(_start));

  cout << start << endl;

  cout << ans(start) << endl;


  return 0;
}
