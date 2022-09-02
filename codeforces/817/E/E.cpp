#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>

using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int N, Q;
vector<pair<int, int>> rectangles;
vector<pair<pair<int, int>, pair<int, int>>> queries;
int K;

int weights[2009][2009];
int prefix[2009][2009];

i32 main() {

  int T;
  cin >> T;
  while (T --> 0) {
    rectangles.clear();
    queries.clear();
    K = 0;

    cin >> N >> Q;

    for (int i=0; i<N; i++) {
      int x, y;
      cin >> x >> y;
      x *= 2; y *= 2;
      K = max(K, x); K = max(K, y);
      rectangles.push_back({x, y});
    }
    for (int i=0; i<Q; i++) {
      int x, y, X, Y;
      cin >> x >> y >> X >> Y;
      x = 2*x + 1;
      y = 2*y + 1;
      X = 2*X - 1;
      Y = 2*Y - 1;
      K = max(K, x); K = max(K, y); K = max(K, X); K = max(K, Y);
      queries.push_back({{x, y}, {X, Y}});
    }

    K++;
    for (int i=0; i<K; i++) for (int j=0; j<K; j++) {
      weights[i][j] = prefix[i][j] = 0;
    }

    for (auto& [x, y] : rectangles) weights[x][y] += x*y;

    for (int i=1; i<K; i++) for (int j=1; j<K; j++) {
      prefix[i][j] = weights[i][j] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1];
    }

    for (auto p : queries) {
      auto& [x, y] = p.first;
      auto& [X, Y] = p.second;
      int r =  prefix[X][Y] - prefix[x][Y] - prefix[X][y] + prefix[x][y];
      cout << (r / 4) << endl;
    }
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS