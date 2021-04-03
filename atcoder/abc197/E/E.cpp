#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

template<class T> void sort_unique(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()),v.end());}

int N;
vector<int> cs;
vector<int> xs_of_c[200009];
vector<pair<int, int>> intervals;

long long memo[200009][2];

long long ans(int i, int last) {
  if (i == intervals.size()) {
    if (last == 0) return abs(intervals[i-1].first);
    return abs(intervals[i-1].second);
  }
  if (memo[i][last] != -1) return memo[i][last];
  int last_x;
  if (i > 0) {
    pair<int, int> li = intervals[i-1];
    last_x = (last == 0) ? li.first : li.second;
  } else {
    last_x = 0;
  }

  long long d = abs(intervals[i].first - intervals[i].second);

  long long c1 = abs(last_x - intervals[i].first) + d + ans(i+1, 1);
  long long c2 = abs(last_x - intervals[i].second) + d + ans(i+1, 0);

  return memo[i][last] = min(c1, c2);
}

int main() {

  memset(memo, -1, sizeof(memo));

  cin >> N;
  for (int i=0; i<N; i++) {
    int x, c;
    cin >> x >> c;
    cs.push_back(c);
    xs_of_c[c].push_back(x);
  }

  sort_unique(cs);

  for (const auto c : cs) {
    auto l = *min_element(xs_of_c[c].begin(), xs_of_c[c].end());
    auto r = *max_element(xs_of_c[c].begin(), xs_of_c[c].end());
    intervals.push_back({l, r});
  }

  cout << ans(0, 0) << endl;

  return 0;
}
