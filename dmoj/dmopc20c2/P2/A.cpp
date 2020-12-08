#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

int N, M;

int main() {
  cin >> N >> M;
  vector<int> left(1000009, -1);
  vector<int> right(1000009, -1);

  for (int i=0; i<N; i++) {
    int a;
    cin >> a;

    right[a] = i;
    if (left[a] == -1) left[a] = i;
  }

  int ret = 0;

  for (int i=0; i<M; i++) {
    int a, b;
    cin >> a >> b;
    if (right[b] != -1 && left[a] != -1) {
      ret = max(ret, right[b] - left[a] + 1);
    }
  }

  cout << ret << endl;

  return 0;
}
