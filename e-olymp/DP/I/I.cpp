#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> void sort_unique(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()),v.end());}

constexpr int MAX_N = 1000009;
int N;
long long A[MAX_N];
long long memo[MAX_N][2];

long long ans(int i, bool last_robbed) {
  if (i == N) return 0;

  if (memo[i][last_robbed] != -1) return memo[i][last_robbed];

  if (last_robbed) return memo[i][last_robbed] = ans(i+1, false);
  if (i == N-1) return memo[i][last_robbed] = A[i];
  return memo[i][last_robbed] = max(
    ans(i+1, false),
    A[i] + ans(i+1, true)
  );
}

int main() {

  cin >> N;
  for (int i=0; i<N; i++) {
    memo[i][0] = memo[i][1] = -1;
    cin >> A[i];
  }

  cout << ans(0, false) << endl;



  return 0;
}
