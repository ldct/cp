#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

int N, M;
vector<int> A;
vector<int> B;
int memo[1009][1009];

int min3(int a, int b, int c) { return min(a, min(b, c)); }

int match(int x, int y) {
  if (x == y) return 0;
  return 1;
}

int ans(int a, int b) {
  if (a == N) return M-b;
  if (b == M) return N-a;
  if (memo[a][b] != -1) return memo[a][b];

  return memo[a][b] = min3(
    match(A[a],B[b]) + ans(a+1,b+1),
    1 + ans(a+1,b),
    1 + ans(a,b+1)
  );
}

int main() {
  memset(memo, -1, sizeof(memo));

  cin >> N >> M;

  int a,b;

  for (int i=0; i<N; i++) { cin >> a; A.push_back(a); }
  for (int i=0; i<M; i++) { cin >> b; B.push_back(b); }

  cout << ans(0, 0) << endl;

  return 0;
}