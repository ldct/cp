// Robot Instructions

#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t
struct pair_hash {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1,T2> &p) const {
        auto h1 = std::hash<T1>{}(p.first);
        auto h2 = std::hash<T2>{}(p.second);

        // Mainly for demonstration purposes, i.e. works but is overly simple
        // In the real world, use sth. like boost.hash_combine
        return h1*239 + h2;
    }
};

template<typename K, typename V> class hashmap {
public:
    hashmap() = default;
    V& operator[](const K& k) {
        for (uint i = hash(k);; (i += 1) &= (N - 1)) {
            if (not m_used.test(i)) {
                m_keys[i] = k, m_used.set(i);
                return m_vals[i] = V{};
            }
            if (m_keys[i] == k) { return m_vals[i]; }
        }
    }
    static constexpr int LG = 20;
    static constexpr int N = 1 << LG;
    static constexpr unsigned long long r = 11995408973635179863ULL;
    static constexpr uint hash(const unsigned long long a) { return (a * r) >> (64 - LG); }
    static constexpr uint hash(const pair<long long, long long> p) {
        auto h1 = hash(p.first);
        auto h2 = hash(p.second);

        return h1*239 + h2;
    }
    std::bitset<N> m_used;
    K m_keys[N];
    V m_vals[N];
};

int N, n, xg, yg;
vector<pair<int, int>> instructions1, instructions2;
hashmap<pair<int, int>, vector<int>> achievable;
vector<int> ret;

void bump(vector<int>& lst, int l) {
  for (int i=0; i<lst.size(); i++) {
    if (i + l < N+1) {
      ret[i+l] += lst[i];
    }
  }
}

pair<int, int> total(int mask, vector<pair<int, int>>& vec) {
  int x = 0;
  int y = 0;
  for (int i=0; i<vec.size(); i++) {
    if (mask & (1 << i)) {
      x += vec[i].first;
      y += vec[i].second;
    }
  }
  return {x, y};
}

i32 main() {

  cin >> N >> xg >> yg;
  ret = vector<int>(N+1, 0);
  n = N / 2;

  for (int i=0; i<n; i++) {
    int x, y;
    cin >> x >> y;
    instructions1.push_back({x, y});
  }
  for (int i=0; i<N-n; i++) {
    int x, y;
    cin >> x >> y;
    instructions2.push_back({x, y});
  }

  for (uint32_t i=0; i<(1<<instructions1.size()); i++) {
    auto t = total(i, instructions1);
    if (achievable[t].size() == 0) {
      achievable[t] = vector<int>(instructions1.size()+1, 0);
    }
    achievable[t][__builtin_popcount(i)] += 1;
  }

  for (uint32_t i=0; i<(1<<instructions2.size()); i++) {
    auto t = total(i, instructions2);

    int x = xg - t.first;
    int y = yg - t.second;

    pair<int, int> p = {x, y};

    if (achievable[p].size() > 0) {
        bump(achievable[p], __builtin_popcount(i));
    }
  }

  for (int i=1; i<=N; i++) {
    cout << ret[i] << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS