#include <bits/stdc++.h>
using namespace std;

long long minMoves(vector<int>& nums, long long k) {
    vector<long> A, B(1);
    for (int i = 0; i < nums.size(); ++i)
        if (nums[i])
            A.push_back(i);
    long long n = A.size(), res = 2e9;
    for (int i = 0; i < n; ++i)
        B.push_back(B[i] + A[i]);
    for (int i = 0; i < n - k + 1; ++i)
        res = min(res, B[i + k] - B[k / 2 + i] - B[(k + 1) / 2 + i] + B[i]);
    res -= (k / 2) * ((k + 1) / 2);
    return res;
}

int main() {

  string S;
  long long K;
  cin >>
  cout << N << endl;

  return 0;
}
