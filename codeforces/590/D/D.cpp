#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

template<typename T>
class RangeFreqQuery {
public:
  unordered_map<T, vector<int>> store;

  RangeFreqQuery(vector<T>& arr) {
    for (int i=0; i<arr.size(); i++) store[arr[i]].push_back(i);
  }

  int query(int left, int right, T element) {
    int a = lower_bound(store[element].begin(), store[element].end(), left) - store[element].begin();
    int b = upper_bound(store[element].begin(), store[element].end(), right) - store[element].begin();

    return b-a;
  }
};

i32 main() {

  string S;
  cin >> S;
  int Q;
  cin >> Q;
  while (Q --> 0) {

  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS