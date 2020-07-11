#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_K = ;
constexpr size_t MAX_K = 305;
constexpr size_t NUM_CHORDS = 305;

constexpr int MODULUS = 1000000007;

long long memo[MAX_N][NUM_CHORDS][MAX_K];

vector<set<pair<int,int>>> neighbours(NUM_CHORDS);

int N, M, K;

long long ans(int length, int last, int target) {
  if (length == 1) {
    if (target == 0) return 1;
    return 0;
  }
  if (target < 0) return 0;

  if (memo[length][last][target] != -1) return memo[length][last][target];

  long long ret = 0;
  for (auto const& p : neighbours[last]) {
    auto prev = p.first;
    auto cost = p.second;

    ret += ans(length-1, prev, target-cost);
    ret = ret % MODULUS;
  }

  return memo[length][last][target] = ret;
}

int main() {
  cin >> N >> M >> K;

  for (int i=0; i<=N; i++) {
    for (int j=0; j<=300; j++) {
      for (int k=0; k<=MAX_K; k++) {
        memo[i][j][k] = -1;
      }
    }
  }

  for (int i=0; i<M; i++) {
    int P, Q, C;
    cin >> P >> Q >> C;
    neighbours[Q].insert(make_pair(P, C));
  }

  int ret = 0;
  for (int v=1; v<=300; v++) {
    ret += ans(N, v, K);
    ret = ret % MODULUS;
  }

  cout << ret << endl;

  return 0;
}
