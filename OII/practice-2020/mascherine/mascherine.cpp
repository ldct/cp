#include <vector>
#include <iostream>

using namespace std;

int diff(int a, int b, int K) {
  for (int k=1; k<=K; k++) {
    if ((k != a) && (k != b)) return k;
  }
  return -1;
}

int score12(vector<int>& C) {
  int ret = 0;
  int start = 1;
  for (int i=0; i<C.size(); i++) {
    if (start != C[i]) ret++;
    start = 3 - start;
  }
  return ret;
}

int score21(vector<int>& C) {
  int ret = 0;
  int start = 2;
  for (int i=0; i<C.size(); i++) {
    if (start != C[i]) ret++;
    start = 3 - start;
  }
  return ret;
}

void riprogramma(int N, int K, vector<int>& C) {
  if (N == 2) {
    if (C[0] == C[1]) {
      C[0] = 3 - C[1];
      return;
    }
  } else if (K >= 3) {
    C.push_back(-1);
    N++;
    for (int i=0; i<N; i++) {
      if (C[i] == C[i-1]) {
        C[i] = diff(C[i-1], C[i+1], K);
      }
    }
    C.pop_back();
    return;
  } else if (K == 2) {
    int start;
    if (score12(C) > score21(C)) {
      start = 2;
    } else {
      start = 1;
    }
    for (int i=0; i<N; i++) {
      C[i] = start;
      start = 3 - start;
    }
  }
}
