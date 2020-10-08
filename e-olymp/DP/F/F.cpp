#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> void sort_unique(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()),v.end());}

constexpr int MAX_N = 109;
int N;
vector<int> pos;
long long memo[MAX_N][2];

long long ans(int i, bool matched) {
  if (i >= N) return 0;
  if (i == N-1) {
    if (matched) return 0;
    return 100000;
  }
  
  if (memo[i][matched] != -1) return memo[i][matched];

  if (matched) return memo[i][matched] = min(
    pos[i+1] - pos[i] + ans(i+1, true),
    ans(i+1, false)
  );
  return memo[i][matched] = pos[i+1] - pos[i] + ans(i+1, true);
}

int main() {

  cin >> N;

  for (int i=0; i<N; i++) {
    memo[i][0] = memo[i][1] = -1;
    
    int x;
    cin >> x;
    pos.push_back(x);
  }

  sort_unique(pos);
  N = pos.size();

  cout << ans(0, false) << endl;

  return 0;
}
