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

struct UF {
    vector<int> e;
    int N;
    UF(int n) : e(n, -1) {
        N = n;
    }
    bool sameSet(int a, int b) { return find(a) == find(b); }
    int size(int x) { return -e[find(x)]; }
    int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
    bool join(int a, int b) {
        a = find(a), b = find(b);
        if (a == b) return false;
        if (e[a] > e[b]) swap(a, b);
        e[a] += e[b]; e[b] = a;
        return true;
    }
    vector<int> sizes() {
        vector<int> ret;
        for (int i=0;i<N; i++) {
            if (e[i] < 0) ret.push_back(-e[i]);
        }
        sort(ret.begin(), ret.end());
        reverse(ret.begin(), ret.end());
        return ret;
    }
    int max_size(int k) {
        auto _sizes = sizes();
        int ret = 0;
        for (int i=0; i<min(k, (int)_sizes.size()); i++) {
            ret += _sizes[i];
        }
        return ret;
    }
};

int N, D;

int main() {

    cin >> N >> D;

    auto uf = UF(N);

    int extra = 0;

    for (int i=0; i<D; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        if (!uf.join(u, v)) extra++;
        cout <<  (uf.max_size(extra+1) - 1) << endl;
        // cout << uf.sizes() << (uf.max_size(extra+1) - 1) << " " << extra << endl;
    }
    return 0;
}
