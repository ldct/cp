#pragma GCC optimize "Ofast"
#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }


template<size_t N=200009>
class BCCounter {
public:
    long long f[N];
    long long ff[N];
    BCCounter() {
        for (int i=0; i<N; i++) f[i] = ff[i] = 0;
        ff[0] = N;
    }
    void inc(int idx) {
        auto v = f[idx];
        ff[v] -= 1;
        f[idx] += 1;
        ff[v+1] += 1;
    }
    void decr(int idx) {
        auto v = f[idx];
        ff[v] -= 1;
        f[idx] -= 1;
        ff[v-1] += 1;
    }
    int num_nonzero() {
        return N - ff[0];
    }
};

bool ok(BCCounter<>& c, int side) {
  return c.ff[side] == side;
}

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
    int sret = 0;
    int square = side*side;
    // cout << "testing size " << square << endl;

    auto c = BCCounter();
    for (int i=0; i<square; i++) {
      c.inc(B[i]);
    }

    if (ok(c, side)) sret++;

    int i=0;
    int j=square;

    while (j < B.size()) {
      c.decr(B[i]);
      c.inc(B[j]);

      if (ok(c, side)) sret++;

      i++; j++;
    }
    // cout << sret << endl;
    ret += sret;
  }

  cout << ret << endl;


  return 0;
}
