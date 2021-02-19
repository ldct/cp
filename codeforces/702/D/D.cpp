#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

int N, K;
vector<long long> A;

bool ok(long long t) {
  // whether we can have the ans > t
  vector<long long> deltas;
  for (const auto a : A) {
    if (a > t) {
      deltas.push_back(1);
    } else {
      deltas.push_back(-1);
    }
  }
  vector<long long> P = {0};
  for (const auto d : deltas) {
    P.push_back(P[P.size()-1] + d);
  }
  // cout << P << endl;

  auto maxTree = vector<long long>(P);

  for (int i=P.size()-2; i>=0; i--) {
    maxTree[i] = max(maxTree[i], maxTree[i+1]);
  }

  for (int i=0; i<P.size(); i++) {
    int j = i + K;
    if (j >= P.size()) return false;
    if (maxTree[j] - P[i] > 0) return true;
  }
  return false;
}

int main() {

  cin >> N >> K;
  for (int i=0; i<N; i++) {
    long long a;
    cin >> a;
    A.push_back(a);
  }

  // cout << A << endl;

  long long low = 0;
  long long high = 200009;

  assert(ok(low));
  assert(!ok(high));

  while (high - low > 2) {
    assert(ok(low));
    assert(!ok(high));

    long long mid = (low + high) / 2;
    if (ok(mid)) {
      low = mid;
    } else {
      high = mid;
    }
  }

  for (long long t = low;; t++) {
    if (!ok(t)) {
      cout << t << endl;
      return 0;
    }
  }

  return 0;
}
