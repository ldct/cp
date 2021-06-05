#include <bits/stdc++.h>
using namespace std;

using ull = unsigned long long;

struct PolyHash {
    static constexpr int mod = (int)1e9+123; // prime mod of polynomial hashing
    static vector<int> pow1;        // powers of base modulo mod
    static vector<ull> pow2;        // powers of base modulo 2^64
    static int base;                     // base (point of hashing)

    static void gen_base() {
        auto seed = chrono::high_resolution_clock::now().time_since_epoch().count();
        mt19937 mt_rand(seed);
        int _base = uniform_int_distribution<int>(257, mod)(mt_rand);
        base = _base % 2 == 0 ? base-1 : base;
    }


    vector<int> pref1; // Hash on prefix modulo mod
    vector<ull> pref2; // Hash on prefix modulo 2^64

    PolyHash(const std::string& s) : pref1(s.size()+1u, 0) , pref2(s.size()+1u, 0) {
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

    // Polynomial hash of subsequence [pos, pos+len)
    pair<int, ull> operator()(const int pos, const int len) const {
        int hash1 = pref1[pos+len] - pref1[pos];
        ull hash2 = pref2[pos+len] - pref2[pos];
        if (hash1 < 0) hash1 += mod;
        return make_pair(hash1, hash2);
    }
};

vector<int> PolyHash::pow1{1};
vector<ull> PolyHash::pow2{1};
