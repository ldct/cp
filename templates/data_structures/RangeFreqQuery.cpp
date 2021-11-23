#include <bits/stdc++.h>
using namespace std;



class RangeFreqQuery {
public:
  unordered_map< int, vector<int> > store;

  RangeFreqQuery(vector<int>& arr) {
      for (int i=0; i<arr.size(); i++)
        store[arr[i]].push_back(i);
  }

  int query(int left, int right, int element) {
    int a = lower_bound(store[element].begin(),
                        store[element].end(),
                        left)
            - store[element].begin();

    int b = upper_bound(store[element].begin(),
                        store[element].end(),
                        right)
            - store[element].begin();

    return b-a;
  }
};

int main() {

    vector<int> arr = {12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56};
    RangeFreqQuery rangeFreqQuery = RangeFreqQuery(arr);
    cout << rangeFreqQuery.query(1, 2, 4) << endl;
    cout << rangeFreqQuery.query(0, 11, 33) << endl;

  return 0;
}
