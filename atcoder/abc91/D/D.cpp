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

int N;
vector<int> A, B;

int count(vector<int>& B, int a, int b) {
  return upper_bound(B.begin(), B.end(), b) - lower_bound(B.begin(), B.end(), a);
}

int count_pairs(int k) {
  int T = 1 << k;
  vector<int> sA, sB;

  for (auto b : B) sB.push_back(b % (2*T));

  sort(sB.begin(), sB.end());

  int ret = 0;
  
  for (auto aa : A) {
    auto a = aa % (2*T);

    ret += count(sB, T-a, 2*T-1-a);
    ret += count(sB, 3*T-a, 4*T-a);
  }

  return ret;
}

i32 main() {

  cin >> N;
  
  A = vector<int>(N, 0);
  B = vector<int>(N, 0);

  for (int i=0; i<N; i++) {
    cin >> A[i];
  }

  for (int i=0; i<N; i++) {
    cin >> B[i];
  }

  int ret = 0;
  for (int k=0; k<29; k++) {
    if (count_pairs(k) % 2 == 1) {
      ret += (1 << k);
    }
  }

  cout << ret << endl;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS