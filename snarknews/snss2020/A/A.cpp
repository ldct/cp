#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

int N;
vector<pair<int, int>> xs;
vector<pair<int, int>> ys;

vector<pair<int, int>> pxs;
vector<pair<int, int>> pys;


int main() {
  
  cin >> N;
  for (int i=0; i<N; i++) {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    xs.push_back({2*x1,  +2});
    xs.push_back({x1+x2, -2});
    xs.push_back({2*x2,  +2});
    ys.push_back({2*y1,  +2});
    ys.push_back({y1+y2, -2});
    ys.push_back({2*y2,  +2});
    pxs.push_back({2*x1, 2*x2});
    pys.push_back({2*y1, 2*y2});
  }

  sort(xs.begin(), xs.end());
  sort(ys.begin(), ys.end());

  long long x_best_score = LLONG_MAX;

  long long slope = -1LL * N;
  long long score = 0;
  int last_x = xs[0].first;

  for (const auto& p : pxs) {
    score += (p.first - last_x);
  }

  x_best_score = min(x_best_score, score);

  for (const auto& p : xs) {
    auto x = p.first;
    if (x != last_x) {
      score += (slope * (x - last_x));
      x_best_score = min(x_best_score, score);
      last_x = x;
    }
    slope += p.second;
  }

  x_best_score = min(x_best_score, score);

  long long y_best_score = LLONG_MAX;


  slope = -1LL * N;
  score = 0;
  int last_y = ys[0].first;

  for (const auto& p : pys) {
    score += (p.first - last_y);
  }

  y_best_score = min(y_best_score, score);

  for (const auto& p : ys) {
    auto y = p.first;
    if (y != last_y) {
      score += (slope * (y - last_y));
      y_best_score = min(y_best_score, score);
      last_y = y;
    }
    slope += p.second;
  }

  y_best_score = min(y_best_score, score);



  cout << (x_best_score + y_best_score) / 2 << endl;

  return 0;
}
