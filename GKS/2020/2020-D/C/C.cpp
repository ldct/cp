#include <bits/stdc++.h>
using namespace std;

template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

constexpr size_t MAX_N = 500009;

long long T, N, A, B;
int parent[MAX_N];
vector<int> children[MAX_N];

long long num_A[MAX_N];
long long num_B[MAX_N];

void dfs(int u, vector<int>& ancestors) {

  num_A[u] = 1;
  num_B[u] = 1;

  ancestors.push_back(u);
  for (const auto& v : children[u]) dfs(v, ancestors);
  
  if (ancestors.size() >= A+1) num_A[ancestors[ancestors.size() - A - 1]] += num_A[u];
  if (ancestors.size() >= B+1) num_B[ancestors[ancestors.size() - B - 1]] += num_B[u];
  
  ancestors.pop_back();
}

double ans() {

  vector<int> ancestors;
  dfs(0, ancestors);

  long long ans = 0;

  for (int u=0; u<N; u++) {
    ans += (num_A[u] + num_B[u])*N;
    ans -= (num_A[u]*num_B[u]);
  }

  return (double) ans / (N*N);
}

int main() {
  
  cin >> T;
  
  for (int t=1; t<=T; t++) {
    cin >> N >> A >> B;

    for (int i=0; i<N; i++) {
      children[i].clear();
      num_A[i] = num_B[i] = 0;     
    }

    for (int i=0; i<N-1; i++) {
      int p;
      cin >> p;
      p--;
      parent[i+1] = p;
      children[p].push_back(i+1);
    }
    cout << "Case #" << t << ": " << setprecision(17) << ans() << endl;
  }
    
  return 0;
}
