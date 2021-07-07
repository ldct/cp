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


int modinv(int a, int b) {
	int b0 = b, t, q;
	int x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}


using ull = unsigned long long;
int base;
struct PolyHash {
    static constexpr int mod = (int)1e9+123; // prime mod of polynomial hashing
    static vector<int> pow1;        // powers of base modulo mod
    static vector<ull> pow2;        // powers of base modulo 2^64

    static void gen_base() {
        auto seed = chrono::high_resolution_clock::now().time_since_epoch().count();
        mt19937 mt_rand(seed);
        int _base = uniform_int_distribution<int>(257, mod)(mt_rand);
        base = _base % 2 == 0 ? _base-1 : _base;
    }

    vector<int> pref1; // Hash on prefix modulo mod
    vector<ull> pref2; // Hash on prefix modulo 2^64

    PolyHash(const vector<int>& s) : pref1(s.size()+1u, 0) , pref2(s.size()+1u, 0) {
        assert(base < mod);
        const int n = s.size(); // Firstly calculated needed power of base:
        while ((int)pow1.size() <= n) {
            pow1.push_back(1LL * pow1.back() * base % mod);
            pow2.push_back(pow2.back() * base);
        }
        for (int i = 0; i < n; ++i) { // Fill arrays with polynomial hashes on prefix
            assert(base > s[i]);
            pref1[i+1] = (pref1[i] + 1LL * s[i] * pow1[i]) % mod;
            pref2[i+1] = pref2[i] + s[i] * pow2[i];
        }
    }

    pair<int, ull> call(const int pos, const int len) const {
        int hash1 = pref1[pos+len] - pref1[pos];
        ull hash2 = pref2[pos+len] - pref2[pos];

        if (hash1 < 0) hash1 += mod;
        hash1 *= modinv(pow1[pos], mod);
        hash1 %= mod;
        hash1 += mod;
        hash1 %= mod;
        return make_pair(hash1, hash2);
    }

    // Polynomial hash of subsequence [pos, pos+len)
    pair<int, ull> operator()(const int pos, const int len) const {
        return call(pos, len);
    }

    set<pair<int, ull>> substrings(int ssl) const {
        set<pair<int, ull>> ret;
        for (int j=0; j<pref1.size()-ssl; j++) {
            cout << "updating " << call(j, ssl) << endl;
            ret.insert(call(j, ssl));
        }
        cout << endl;
        return ret;
    }
};

vector<int> PolyHash::pow1{1};
vector<ull> PolyHash::pow2{1};

class Solution {
public:
    vector<PolyHash> hashes;

    bool has_ss(int ssl) {
        map<pair<int, ull>, int> freq;
        for (int i=0; i<hashes.size(); i++) {
            for (const auto& h : hashes[i].substrings(ssl)) {
                freq[h]++;
            }
            cout << endl;
        }
        for (const auto& k : freq) {
            if (k.second == hashes.size()) return true;
        }
        return false;
    }

    int longestCommonSubpath(int n, vector<vector<int>>& paths) {
        PolyHash::gen_base();
        for (int i=0; i<paths.size(); i++) for (int j=0; j<paths[i].size(); j++) paths[i][j]++;
        for (int i=0; i<paths.size(); i++) {
            hashes.push_back(PolyHash(paths[i]));
        }
        cout << has_ss(1) << endl;
        cout << has_ss(4) << endl;
        return 42;
    }
};

int main() {
    auto S = Solution();
    vector<int> a = {0,1,2,3,4};
    vector<int> b = {1,2,3};
    vector<int> c =  {4,0,1,2,3};
    vector<vector<int>> paths = {a, b, c};
    cout << S.longestCommonSubpath(5, paths) << endl;

    cout << PolyHash::pow1 << endl;
}
