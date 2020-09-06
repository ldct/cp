#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<int> A;
vector<pair<int, pair<int, int>>> ops;

void swap(vector<int>& A, int x, int y) {
  int tmp = A[x];
  A[x] = A[y];
  A[y] = tmp;
}

int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  
  cin >> N >> M;
  for (int i=1; i<=N; i++) {
    A.push_back(i);
  }
  
  int last_12 = -1;

  for (int i=0; i<M; i++) {
    int t;
    cin >> t;

    int x = -1;
    int y = -1;
    
    if (t == 3) {
      cin >> x >> y;
    }
    ops.push_back({t, {x, y}});

    if (t == 1 || t == 2) last_12 = i;
  }

  if (last_12 != -1) {
    // apply
    auto p = ops[last_12];
    assert(p.first == 1 || p.first == 2);
    sort(A.begin(), A.end());
    if (p.first == 2) {
      reverse(A.begin(), A.end());
    }
  }

  bool reversed = false;

  for (int i=last_12+1; i<ops.size(); i++) {
    auto p = ops[i];

    assert(p.first == 3 || p.first == 4);

    if (p.first == 3) {
      int x = p.second.first;
      int y = p.second.second;
      x--; y--;
      if (reversed) {
        x = A.size() - 1 - x;
        y = A.size() - 1 - y;
      }
      swap(A, x, y);
    } else {
      reversed = !reversed;
    }

  }

  if (reversed) {
    reverse(A.begin(), A.end());
  }

  for (int i=0; i<A.size(); i++) {
    if (i > 0) cout << " ";
    cout << A[i];
  }
  cout << endl;
    
  return 0;
}
