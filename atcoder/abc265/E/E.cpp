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

constexpr int MODULUS = 998244353;
int N, M;
int A, B, C, D, E, F;

set<pair<int,int>> obstacles;

i32 main() {

  cin >> N >> M >> A >> B >> C >> D >> E >> F;
  vector<pair<int,int>> directions = {{A,B}, {C,D}, {E,F}};

  for (int i=0; i<M; i++) {
    int x, y;
    cin >> x >> y;
    obstacles.insert({x, y});
  }

  map<pair<int,int>, int> paths;
  paths[{0,0}] = 1;

  for (int i=0; i<N; i++) {
    map<pair<int,int>,int> next_paths;

    for (auto p : paths) {
      auto x = p.first.first;
      auto y = p.first.second;
      for (auto p2 : directions) {
            int xx = x + p2.first;
            int yy = y + p2.second;
            if (obstacles.count({xx,yy})) continue;
            next_paths[{xx,yy}] += paths[p.first];
            next_paths[{xx,yy}] %= MODULUS;
      }
    }

    paths = next_paths;
  }

  int ret = 0;
  for (auto p : paths) {
    ret += p.second;
    ret %= MODULUS;
  }
  cout << ret << endl;



  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS