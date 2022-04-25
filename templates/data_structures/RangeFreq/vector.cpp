#include <bits/stdc++.h>
using namespace std;

// 1026ms on https://judge.yosupo.jp/problem/static_range_frequency

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

int main() {

  int N, Q;
  cin >> N >> Q;
  vector<int> arr;
  while (N --> 0) {
    int a;
    cin >> a;
    arr.push_back(a);
  }
  RangeFreqQuery rangeFreqQuery = RangeFreqQuery(arr);
  while (Q --> 0) {
    int l, r, x;
    cin >> l >> r >> x;
    cout << rangeFreqQuery.query(l, r-1, x) << endl;
  }

  return 0;
}