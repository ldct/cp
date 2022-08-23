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

int c1[MAX_N];
int c2[MAX_N];

void dfs1(int u, int daddy) {
  if (v1[u] != -1) return;
  cout << "visit " << u << endl;
  v1[u] = 1;
  for (auto v : n1[u]) {
    dfs1(v, daddy);
  }
}

i32 main() {

  memset(v1, -1, sizeof(v1));
  memset(v2, -1, sizeof(v2));

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

  for (int i=1; i<=N; i++) {
    if (c1[i] == -1) dfs1(1, 1);
  }

  for (int i=1; i<=N; i++) {
    cout << c1[i] << endl;
  }  

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS