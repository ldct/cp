#include "paint.h"
#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }

vector<set<int>> contractors_of_col;

bool ok(int N, int M, vector<int>& C, vector<set<int>>& B, int c, int b) {
  for (int k=0; k<M; k++) {
    int i = (c+k) % N;
    int j = (b+k) % M;

    // cout << "checking " << i << " " << j << endl;

    if (B[j].count(C[i]) == 0) {
      // cout << "bad" << endl;
      return false;
    }
  }

  return true;
}

int minimumInstructions(
  int N, int M, int K, vector<int> C,
  vector<int> A, vector<vector<int>> B
) {

  vector<set<int>> BB;
  for (int m=0; m<M; m++) {
    BB.push_back(set<int>(B[m].begin(), B[m].end()));
  }

  for (int k=0; k<K; k++) {
    contractors_of_col.push_back(set<int>());
  }

  for (int m=0; m<M; m++) {
    for (const auto& col : B[m]) {
      contractors_of_col[col].insert(m);
    }
  }

  // cout << contractors_of_col << endl;

  vector<int> ok_indices;

  for (int c=0; c<N; c++) {
    for (int b=0; b<M; b++) {
      if (ok(N, M, C, BB, c, b)) {
        ok_indices.push_back(c);
        break;
      }
    }
  }

  if (ok_indices.size() == 0) return -1;

  int ret = INT_MAX;

  for (int start=0; start<ok_indices.size(); start++) {
    vector<int> flush;
    for (int k=0; k<ok_indices.size(); k++) {
      int j = (start+k) % ok_indices.size();
      flush.push_back(ok_indices[j]);
    }
    int offset = flush[0];
    for (auto& j : flush) {
      j -= offset;
      j = (j%N + N) % N;
    }
    // cout << "start=" << start << " flush=" << flush << endl;

    int last = 0;
    int cost = 1;
    for (int i=0; i<flush.size(); i++) {
      if ((i-last) >= M) {
        last = i-1;
        cost++;
        i--;
      }
    }

    ret = min(ret, cost);
  }

  return ret;
}
