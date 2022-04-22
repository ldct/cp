#include <bits/stdc++.h>
using namespace std;

#define int long long
#define i32 int32_t
#define i64 int64_t

// a small, fast replacement for std::unordered_map
template<typename K, typename V> class hashmap {
public:
    static constexpr int LG = 20;
    static constexpr int N = 1 << LG;
    static constexpr uint hash(const i64 a) {
        return (a % N);
    }
    hashmap() = default;
    V& operator[](const K& k) {
        for (uint i = hash(k);;i++) {
            if (!m_used.test(i)) {
                m_keys[i] = k, m_used.set(i);
                return m_vals[i] = V{};
            }
            if (m_keys[i] == k) { return m_vals[i]; }
        }
    }
    bitset<N> m_used;
    vector<K> m_keys = vector<K>(N);
    vector<V> m_vals = vector<V>(N);
};

i32 main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    hashmap<i64, i64> dict;

    int q; cin >> q; while (q --> 0) {
        int t, k, v;
        cin >> t >> k;
        if (t == 0) {
            int v; cin >> v;
            dict[k] = v;
        } else {
            cout << dict[k] << endl;
        }
    }

    return 0;
}