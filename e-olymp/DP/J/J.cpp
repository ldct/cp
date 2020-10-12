#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> void sort_unique(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()),v.end());}

template<class T, class U>
T round_div(const T n, const U d) {
  return ((n < 0) ^ (d < 0)) ? ((n - d/2)/d) : ((n + d/2)/d);
}

constexpr int MAX_N = 100009;
int N, K;
long long temp[MAX_N];

int main() {

  cin >> N >> K;
  for (int i=0; i<N; i++) {
    cin >> temp[i];
  }

  long long sum = 0;
  int i=0;
  int j=0;

  while (j - i != K) {
    sum += temp[j++];
  }

  long long low = LLONG_MAX;
  long long high = LLONG_MIN;

  low = min(low, round_div(sum, K)); high = max(high, round_div(sum, K));

  while (j < N) {
    sum -= temp[i++];
    sum += temp[j++];
    low = min(low, round_div(sum, K)); high = max(high, round_div(sum, K));
  }

  cout << low << endl;
  cout << high << endl;

  return 0;
}
