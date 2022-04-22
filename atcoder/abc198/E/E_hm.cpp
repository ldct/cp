#include <bits/stdc++.h>
using namespace std;

template<typename K, typename V>
class hashmap {
public:
    hashmap() = default;
    V& operator[](const K& k)
    {
        for (uint i = hash(k);; (i += 1) &= (N - 1)) {
            if (not m_used.test(i)) {
                m_keys[i] = k, m_used.set(i);
                return m_vals[i] = V{};
            }
            if (m_keys[i] == k) { return m_vals[i]; }
        }
    }
private:
    static constexpr int LG = 18;
    static constexpr int N = 1 << LG;
    static constexpr unsigned long long r = 11995408973635179863ULL;
    static constexpr uint hash(const unsigned long long a) { return (a * r) >> (64 - LG); }
    std::bitset<N> m_used;
    K m_keys[N];
    V m_vals[N];
};

int N;
int colour[100009];
vector<int> neighbours[100009];
int is_good[100009];

hashmap<int, int> ancestors;

void dfs0(int u, int parent) {

  if (ancestors[colour[u]]) is_good[u] = false;
  ancestors[colour[u]]++;

  for (const auto v : neighbours[u]) {
    if (v == parent) continue;
    dfs0(v, u);
  }

  ancestors[colour[u]]--;
}

int main() {

  ios_base::sync_with_stdio(false); cin.tie(NULL);

  cin >> N;
  for (int i=0; i<N; i++) cin >> colour[i];

  for (int i=0; i<N-1; i++) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    neighbours[u].push_back(v);
    neighbours[v].push_back(u);
  }

  for (int i=0; i<N; i++) is_good[i] = true;

  dfs0(0, -1);

  for (int i=0; i<N; i++) {
    if (is_good[i]) cout << (i+1) << endl;
  }



  return 0;
}
