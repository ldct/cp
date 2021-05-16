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

int N;
vector<pair<long long, long long>> neighbours[200009];
long long path_weight[200009];
vector<long long> ett;
constexpr long long MODULUS = 1000000007;

// sum of xor of pairs
// TAG:xor TAG:pair
long long int sumXOR(vector<long long> arr) { // modifies arr
  long long sum = 0, n = arr.size();
  for (int i = 0; i < 64; i++) {
    long long zc = 0, oc = 0;

    long long idsum = 0;
    for (int j = 0; j < n; j++) {
      if (arr[j] % 2 == 0) zc++; else oc++;
      arr[j] /= 2;
    }

    idsum = oc * (zc * ((1LL << i) % MODULUS) % MODULUS);
    idsum %= MODULUS;

    sum += idsum;
    sum %= MODULUS;
  }
  return sum;
}

void dfs(int u, int parent) {
  for (auto p : neighbours[u]) {
    int v = p.first;
    long long w = p.second;
    if (v == parent) continue;
    path_weight[v] = path_weight[u]^w;
    dfs(v, u);
  }
}

int main() {

  cin >> N;

  memset(path_weight, 0, sizeof(path_weight));

  for (int i=0; i<N-1; i++) {
    long long u, v, w;
    cin >> u >> v >> w;
    u--; v--;
    neighbours[u].push_back({v, w});
    neighbours[v].push_back({u, w});
  }

  dfs(0, -1);

  vector<long long> pw;
  for (int i=0; i<N; i++) {
    pw.push_back(path_weight[i]);
  }

  cout << sumXOR(pw) << endl;

  return 0;
}
