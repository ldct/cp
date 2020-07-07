#include <bits/stdc++.h>

using namespace std;

template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }

constexpr size_t MAX_N = 100001;

int N;
int K;
int T[MAX_N];

int main() {
  
  cin >> N >> K;

  for (int i=0; i<N; i++) {
    cin >> T[i];
  }

  sort(&T[0], &T[N]);

  vector<int> gaps;

  for (int i=0; i<N-1; i++) {
    gaps.push_back(T[i+1] - T[i] - 1);
  }

  sort(gaps.begin(), gaps.end());
  reverse(gaps.begin(), gaps.end());

  // cout << "gaps=" << gaps << endl;

  long long ans = T[N-1] - T[0] + 1;

  // cout << "ans=" << ans << endl;

  for (int i=0; i<N && i<K-1; i++) {
    // cout << "sub " << gaps[i] << endl;
    ans -= gaps[i];
  }

  cout << ans << endl;

  return 0;
}
