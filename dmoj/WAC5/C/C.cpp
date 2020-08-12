#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

int main() { 
  int N;
  cin >> N;
  vector<long long>B(N, 0);
  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    B[i] = a;
  }

  int ret = 0;

  for (int side=1; side*side<= B.size(); side++) {
    int square = side*side;
    // cout << "testing size " << square << endl;

    unordered_map<long long, int> freq;
    for (int i=0; i<square; i++) {
      if (freq.count(B[i]) == 0) freq[B[i]] = 0;
      freq[B[i]]++;
    }

    // if (ok(freq, side)) ret++;

    int i=0;
    int j=0;

    while (j < B.size()) {
      // freq[B[i]]--;
      // if (freq[B[i]] == 0) freq.erase(B[i]);
      // if (freq.count(B[j]) == 0) freq[B[j]] = 0;
      // freq[B[j]]++;

      i++; j++;
    }

    // if (ok(freq, side)) ret++;
  }

  return 0;
}
