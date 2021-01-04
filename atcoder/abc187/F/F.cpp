#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

// todo: this ain't random
unsigned long xor128() {
        static unsigned long x = 123456789, y = 362436069, z = 521288629, w = 88675123;
        unsigned long t = (x ^ (x << 11));
        x = y; y = z; z = w;
        return (w = (w ^ (w >> 19)) ^ (t ^ (t >> 8)));
}
int RandomPrime() {
        auto prime = [&](int n) {
                for (int i = 2; i * i <= n; i ++) if (n % i == 0) return false;
                return true;
        };
        int modulo = 1000000000;
        modulo += (int) (xor128() % 100000000);
        while (!prime(modulo)) modulo ++;
        return modulo;
}

// https://codeforces.com/blog/entry/57496
// https://web.archive.org/web/20180128192034/http://www.learning-algorithms.com/entry/2018/01/27/235959
int ChromaticNumber(const vector<vector<bool>> &tmpg) {
  int n = tmpg.size();
  if (n == 0) return 0;
  vector<int> g(n);
  for (int i = 0; i < n; i ++) {
    for (int j = 0; j < n; j ++) {
      if (tmpg[i][j]) {
        g[i] |= (1 << j);
      }
    }
  }
  int all = 1 << n;
  vector<int> a(all), s(all);
  a[0] = 1;
  int modulo = RandomPrime();
  for (int i = 1; i < all; i ++) {
    int j = __builtin_ctz(i);
    a[i] = a[i - (1 << j)] + a[(i - (1 << j)) & ~g[j]];
    if (a[i] >= modulo) a[i] -= modulo;
  }
  for (int i = 0; i < all; i ++) {
    s[i] = ((n - __builtin_popcount(i)) & 1 ? -1 : 1);
  }
  for (int k = 1; k < n; k ++) {
    long long sum = 0;
    for (int i = 0; i < all; i ++) {
      long long cur = ((s[i] * (long long) a[i]) % modulo);
      s[i] = (int) cur;
      sum += cur;
    }
    if (sum % modulo != 0) return k;
  }
  return n;
}



int N, M;

int main() {

  cin >> N >> M;

  vector<vector<bool>> g;

  for (int i=0; i<N; i++) {
    g.push_back(vector<bool>(N, true));
  }

  for (int i=0; i<M; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    g[a][b] = g[b][a] = false;
  }

  cout << ChromaticNumber(g) << endl;

  return 0;
}
