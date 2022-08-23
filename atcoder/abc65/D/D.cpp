#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>
#include <map>
#include <unordered_map>

/*
map: 177ms
unordered_map is slower...
*/

using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t


struct HASH{
  size_t operator()(const pair<int,int>&x)const{
    return hash<long long>()(
      x.first*239 + x.second
    );
  }
};

constexpr int MAX_N = 200009;

int N, K, L;

vector<int> n1[MAX_N];
vector<int> n2[MAX_N];

int c1[MAX_N];
int c2[MAX_N];

void dfs1(int u, int daddy) {
  if (c1[u] != -1) return;
  c1[u] = daddy;
  for (auto v : n1[u]) {
    dfs1(v, daddy);
  }
}

void dfs2(int u, int daddy) {
  if (c2[u] != -1) return;
  c2[u] = daddy;
  for (auto v : n2[u]) {
    dfs2(v, daddy);
  }
}

i32 main() {

  memset(c1, -1, sizeof(c1));
  memset(c2, -1, sizeof(c2));

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
    if (c1[i] == -1) dfs1(i, i);
  }

  for (int i=1; i<=N; i++) {
    if (c2[i] == -1) dfs2(i, i);
  }

unordered_map<pair<int,int>,int,HASH> cnt;

  for (int i=1; i<=N; i++) {
    cnt[{c1[i], c2[i]}]++;
  }  

  for (int i=1; i<=N; i++) {
    cout << cnt[{c1[i], c2[i]}] << " ";
  }  
  cout << endl;


  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS