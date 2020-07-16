#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_NM = 100000009;

long long N, M;
char string_data[MAX_NM];
long long memo[MAX_NM];

bool possible(long long x, long long y) {
  if (string_data[x*M+y] == '#') return false;
  if (x >= N || y >= M) return false;
  if (x == N-1 && y == M-1) return true;

  if (memo[x*M+y] != -1) return memo[x*M+y];

  return memo[x*M+y] = possible(x+1,y) || possible(x,y+1);
}

int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  
  long long T;
  cin >> T;
  for (long long i=0; i<T; i++) {
    cin >> N >> M;
    for (long long j=0; j<N; j++) {
      for (long long k=0; k<M; k++) {
        char c;
        cin >> c;
        // assert(c == '#' || 'a' <= c <= 'z');
        string_data[j*M+k] = c;
        memo[j*M+k] = -1;
      }
    }

    set<pair<long long,long long>> frontier;
    frontier.insert(make_pair(0,0));

    for (long long k=0; k<M+N-1; k++) {
      char m = 'z';
      for (const auto& p : frontier) {
        auto x = p.first;
        auto y = p.second;
        m = min(m, string_data[x*M+y]);
      }
      cout << m;
      set<pair<long long,long long>> next_frontier;
      for (const auto& p : frontier) {
        auto x = p.first;
        auto y = p.second;
        if (m != string_data[x*M+y]) continue;
        if (possible(x+1,y)) next_frontier.insert(make_pair(x+1,y));
        if (possible(x,y+1)) next_frontier.insert(make_pair(x,y+1));
      }
      frontier = next_frontier;
    }
    cout << endl;
  } 
  return 0;
}
