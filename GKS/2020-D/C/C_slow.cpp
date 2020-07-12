#include <bits/stdc++.h>
using namespace std;

template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

constexpr size_t MAX_N = 500009;

int T, N, A, B;
int parent[MAX_N];

vector<int> path_to_root(int v) {
  vector<int> ret;

  while (v != 0) {
    ret.push_back(v);
    v = parent[v];
  }

  ret.push_back(v);

  return ret;
}

vector<int> py_slice(vector<int>& v, int skip) {
  vector<int> ret;
  for (int i=0; i<v.size(); i+=skip) ret.push_back(v[i]);
  return ret;
}

double ans() {

  long long num_painted = 0;

  for (int u=0; u<N; u++) {
    for (int v=0; v<N; v++) {
      auto A_painted = path_to_root(u);
      auto B_painted = path_to_root(v);

      A_painted = py_slice(A_painted, A);
      B_painted = py_slice(B_painted, B);

      set<int> total;
      total.insert(A_painted.begin(), A_painted.end());
      total.insert(B_painted.begin(), B_painted.end());

      num_painted += total.size();
    }
  }
  return (double) num_painted / (N*N);
}

int main() {
  
  cin >> T;
  
  for (int t=1; t<=T; t++) {
    cin >> N >> A >> B;
    for (int i=0; i<N-1; i++) {
      cin >> parent[i+1];
      parent[i+1]--; 
    }
    cout << "Case #" << t << ": " << setprecision(numeric_limits<double>::max_digits10) << ans() << endl;
  }
    
  return 0;
}
