#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

int N;
int eaten[2009][2009];
vector<int> xs, ys;
map<int, int> compressed_x_of;
map<int, int> compressed_y_of;

struct Cow {
  int id;
  pair<int, int> position;
  pair<int, int> velocity;

  bool alive() {
    return (velocity.first + velocity.second) > 0;
  }

  int av() {
    if (!alive()) return INT_MAX;
    if (velocity.first == 1) {
      int x = position.first;
      if (x == N-1) return INT_MAX;
      return xs[x+1] - xs[x];
    } else {
      int y = position.first;
      if (y == N-1) return INT_MAX;
      return ys[y+1] - ys[y];
    }
  }
  void move() {

  }
};

vector<Cow> cows;

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

    pair<int, int> velocity = {0, 1};
    if (d == 'E') { velocity = {1, 0}; }

    xs.push_back(x); ys.push_back(y);

    Cow c = {i, {x, y}, velocity};
    cows.push_back(c);
  }

  sort(xs.begin(), xs.end());
  sort(ys.begin(), ys.end());

  for (int i=0; i<N; i++) {
    compressed_x_of[xs[i]] = i;
    compressed_y_of[ys[i]] = i;
  }

  for (int i=0; i<N; i++) {
    auto c = cows[i];
    cows[i].position = {compressed_x_of[c.position.first], compressed_y_of[c.position.second]};
  }

  // for (int t=0; t<2009; t++) {

  //   for (int i=0; i<N; i++) {
  //     eaten[c.first][c.second] = i;
  //     coords[i] = { c.first + v.first, c.second + v.second };
  //   }
  //   for (int i=0; i<N; i++) {
  //     auto c = coords[i];
  //     if ((velocity[i].first + velocity[i].second) > 0 && eaten[c.first][c.second] != -1) {

  //       children[eaten[c.first][c.second]].push_back(i);
  //       velocity[i] = {0, 0};
  //     }
  //   }
  // }

  // for (int i=0; i<N; i++) {
  //   cout << ans(i)-1 << endl;
  // }


  return 0;
}
