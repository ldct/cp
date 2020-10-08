#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> void sort_unique(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()),v.end());}

constexpr int MAX_N = 74;
int N;

long long memo[MAX_N][5];

long long ans(int i, int num_white) {
  if (num_white >= 3) return 0;
  if (i == N) return 1;
  if (memo[i][num_white] != -1) return memo[i][num_white];
  return memo[i][num_white] = ans(i+1, 0) + ans(i+1, num_white+1);
}

int main() {

  cin >> N;

  for (int i=0; i<N; i++) for (int j=0; j<5; j++) memo[i][j] = -1;

  cout << ans(0, false) << endl;

  return 0;
}
