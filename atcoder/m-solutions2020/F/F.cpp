#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>

using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

long long N;

map<long long, vector<pair<long long, char>>> forward_diag;
map<long long, vector<pair<long long, char>>> backward_diag;
map<long long, vector<pair<long long, char>>> updown;
map<long long, vector<pair<long long, char>>> leftright;

long long search(vector<pair<long long, char>>& lst, char A, char B, bool skip) {

  long long ret = LLONG_MAX;
  int i=0;
  auto ll = lst.size();
  while (i < ll) {
    while (i < ll && lst[i].second != A) i++;
    auto j = i;
    while (j < ll && lst[j].second != B) j++;
    if (i < ll && j < ll) ret = min(ret, lst[j].first - lst[i].first);
    i++;
  }
  return ret;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL);

  cin >> N;
  vector<pair<pair<long long, long long>, char>> xyU;
  vector<pair<pair<long long, long long>, char>> yxU;

  for (int i=0; i<N; i++) {
    long long x, y;
    char U;
    cin >> x >> y >> U;

    xyU.push_back(make_pair(make_pair(x, y), U));
    yxU.push_back(make_pair(make_pair(y, x), U));
  }

  sort(xyU.begin(), xyU.end());
  sort(yxU.begin(), yxU.end());

  for (auto const& xyu : xyU) {
    long long x = xyu.first.first;
    long long y = xyu.first.second;    
    char U = xyu.second;

    if (forward_diag.count(x-y) == 0) forward_diag[x-y] = vector<pair<long long, char>>();
    forward_diag[x-y].push_back(make_pair(x, U));

    if (backward_diag.count(x+y) == 0) backward_diag[x+y] = vector<pair<long long, char>>();
    backward_diag[x+y].push_back(make_pair(x, U));

    if (leftright.count(y) == 0) leftright[y] = vector<pair<long long, char>>();
    leftright[y].push_back(make_pair(x, U));
  }

  for (auto const& xyu : yxU) {
    long long x = xyu.first.second;
    long long y = xyu.first.first;    
    char U = xyu.second;

    if (updown.count(x) == 0) updown[x] = vector<pair<long long, char>>();
    updown[x].push_back(make_pair(y, U));

  }





  long long min_collisions = LLONG_MAX;

  for (auto& x : updown) {
    auto lst = x.second;
    auto r = search(lst, 'U', 'D', false);
    if (r != LLONG_MAX) min_collisions = min(min_collisions, 5*r);
  }

  for (auto& x : leftright) {
    auto lst = x.second;
    auto r = search(lst, 'R', 'L', false);
    if (r != LLONG_MAX) min_collisions = min(min_collisions, 5*r);
  }

  for (auto& x : forward_diag) {
    auto lst = x.second;
    auto r = search(lst, 'U', 'L', false);
    if (r != LLONG_MAX) min_collisions = min(min_collisions, 10*r);
    r = search(lst, 'R', 'D', true);
    if (r != LLONG_MAX) min_collisions = min(min_collisions, 10*r);
  }

  for (auto& x : backward_diag) {
    auto lst = x.second;
    auto r = search(lst, 'R', 'U', false);
    if (r != LLONG_MAX) min_collisions = min(min_collisions, 10*r);
    r = search(lst, 'D', 'L', true);
    if (r != LLONG_MAX) min_collisions = min(min_collisions, 10*r);
  }

  if (min_collisions == LLONG_MAX) { 
    cout << "SAFE" << endl;
  } else {
    cout << min_collisions << endl;
  }
    
  return 0;
}
