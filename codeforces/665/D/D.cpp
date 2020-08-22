#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

constexpr size_t MAX_N = 100009;
int N;
int M;

constexpr int MODULUS = 1000000007;

vector<int> neighbours[MAX_N];
long long c_sss[MAX_N];

long long ss_size(int u, int parent) {
  long long ret = 0;
  for (const auto& v : neighbours[u]) {
    if (v != parent) {
      ret += ss_size(v, u);
    }
  }
  return c_sss[u] = ret + 1;
}

int main() {
  int T;
  cin >> T;
  while (T --> 0) {
    cin >> N;
    for (int i=0; i<N; i++) {
      neighbours[i].clear();
    }
    for (int i=0; i<N-1; i++) {
      int u, v;
      cin >> u >> v;
      u--; v--;
      neighbours[u].push_back(v);
      neighbours[v].push_back(u);
    }
    cin >> M;
    vector<long long> primes;
    for (int i=0; i<M; i++) {
      int p;
      cin >> p;
      primes.push_back(p);
    }
    ss_size(0, 0);

    vector<long long> edge_weights;
    for (int i=1; i<N; i++) {
      long long s = c_sss[i];
      edge_weights.push_back(s * (N - s));
    }

    sort(edge_weights.begin(), edge_weights.end());
    sort(primes.begin(), primes.end());

    // no more sorting from this point on
    
    for (int i=0; i<edge_weights.size(); i++) {
      edge_weights[i] %= MODULUS;
    }
    for (int i=0; i<primes.size(); i++) {
      primes[i] %= MODULUS;
    }

    long long ret = 0;

    if (primes.size() <= edge_weights.size()) {
      reverse(edge_weights.begin(), edge_weights.end());
      reverse(primes.begin(), primes.end());
      int i=0;
      for (; i<primes.size(); i++) {
        ret += primes[i]*edge_weights[i];
        ret %= MODULUS;
      }
      for (; i<edge_weights.size(); i++) {
        ret += edge_weights[i];
        ret %= MODULUS;
      }
    } else {
      long long e = edge_weights.back(); // heaviest edge
      edge_weights.pop_back();

      long long heavy_factor = 1;
      while (primes.size() != edge_weights.size()) {
        heavy_factor *= primes.back();
        heavy_factor %= MODULUS;
        primes.pop_back();
      }

      ret += heavy_factor*e;
      ret %= MODULUS;

      for (int i=0; i < primes.size(); i++) {
        ret += primes[i]*edge_weights[i];
        ret %= MODULUS;
      }
    }
    cout << ret << endl;
  } 
  return 0;
}
