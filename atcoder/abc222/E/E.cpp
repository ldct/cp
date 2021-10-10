#include <bits/stdc++.h>
using namespace std;

int N, M, K;
int A[109];
vector<int> neighbours[1009];

int main() {

  cin >> N >> M >> K;
  for (int i=0; i<M; i++) cin >> A[i];

  for (int i=0; i<N-1; i++) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    neighbours[u].push_back(v);
    neighbours[v].push_back(u);
  }

  for (int i=0; i<M-1; i++) {
    traver
  }

  cout << N << endl;

  return 0;
}
