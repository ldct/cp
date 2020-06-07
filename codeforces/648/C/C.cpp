#include <bits/stdc++.h>

using namespace std;

constexpr size_t MAX_N = 300000;

int N;

vector<pair<int, int>> A;
vector<pair<int, int>> B;

int main() {
  
  scanf("%d", &N);

  for (int i=0; i<N; i++) {
    int a;
    scanf("%d", &a);
    A.push_back(make_pair(a, i));
  }

  for (int i=0; i<N; i++) {
    int b;
    scanf("%d", &b);
    B.push_back(make_pair(b, i));
  }

  sort(A.begin(), A.end());
  sort(B.begin(), B.end());  
  
  vector<int> misalignments;

  for (int i=0; i<N; i++) {
    auto a_idx = A[i].second;
    auto b_idx = B[i].second;

    misalignments.push_back((b_idx - a_idx + N) % N);
  }

  // for (int i=0; i<N; i++) {
  //   printf("%d ", misalignments[i]);
  // }
  // printf("\n");

  vector<int> freqs;

  for (int i=0; i<N; i++) {
    freqs.push_back(0);
  }

  for (auto m : misalignments) {
    freqs[m] += 1;
  }

  int ans = 0;
  for (auto f : freqs) {
    ans = max(ans, f);
  }
  printf("%d\n", ans);

  return 0;
}
