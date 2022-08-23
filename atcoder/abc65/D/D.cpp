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

constexpr int MAX_N = 200009;

int N, K, L;

vector<int> n1[MAX_N];
vector<int> n2[MAX_N];

short v1[MAX_N];
short v2[MAX_N];

void dfs1(int u) {
  if (v1[u]) return;
  cout << "visit " << u << endl;
  v1[u] = 1;
  for (auto v : n1[u]) {
    dfs1(v);
  }
}

i32 main() {

  memset(v1, 0, sizeof(v1));
  memset(v2, 0, sizeof(v2));

  cin >> N >> K >> L;
  for (int i=0; i<K; i++) {
    int p, q;
    cin >> p >> q;
    n1[p].push_back(q);
    n1[q].push_back(p);
  } 

  for (int i=0; i<L; i++) {
    int p, q;
    cin >> p >> q;
    n2[p].push_back(q);
    n2[q].push_back(p);
  } 

  dfs1(1);
  

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS