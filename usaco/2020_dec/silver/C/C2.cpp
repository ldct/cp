#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

int N;
int eaten[2009][2009];
pair<int, int> velocity[1009];
pair<int, int> coords[1009];

vector<int> children[1009];

long long ans(int u) {
  long long ret = 1;
  for (const auto v : children[u]) {
    ret += ans(v);
  }
  return ret;
}

int main() {

  cin >> N;

  memset(eaten, -1, sizeof(eaten));

  for (int i=0; i<N; i++) {
    char d;
    int x, y;
    cin >> d >> x >> y;
    assert(d == 'E' || d == 'N');
    assert(x < 2009); assert(y < 2009);

    if (d == 'E') {
      velocity[i] = {1, 0};
    } else {
      velocity[i] = {0, 1};
    }
    coords[i] = {x, y};
  }

  for (int t=0; t<2009; t++) {
    for (int i=0; i<N; i++) {
      auto c = coords[i];
      auto v = velocity[i];

      if (c.first > 2005 || c.second > 2005) {
        velocity[i] = {0, 0};
      }

      eaten[c.first][c.second] = i;
      coords[i] = { c.first + v.first, c.second + v.second };
    }
    for (int i=0; i<N; i++) {
      auto c = coords[i];
      if ((velocity[i].first + velocity[i].second) > 0 && eaten[c.first][c.second] != -1) {

        children[eaten[c.first][c.second]].push_back(i);
        velocity[i] = {0, 0};
      }
    }
  }

  for (int i=0; i<N; i++) {
    cout << ans(i)-1 << endl;
  }


  return 0;
}
