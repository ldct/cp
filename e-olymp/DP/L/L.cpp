/*
TAG: k-step fibonacci
*/
#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
template<class T> void sort_unique(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()),v.end());}
template<class T, class U> T round_div(const T n, const U d) { return ((n < 0) ^ (d < 0)) ? ((n - d/2)/d) : ((n + d/2)/d); }

constexpr int MODULUS = 1000000007;
constexpr int MAX_N = 1000009;
int N, K;
long long memo[MAX_N];

long long modexp(long long b, long long e) {
	long long ans = 1;
	for (; e; b = b * b % MODULUS, e /= 2)
		if (e & 1) ans = ans * b % MODULUS;
	return ans;
}

long long F_slow(int n, int k) {
  if (n < 0) return 0;
  if (n == 0) return 1;

  long long ret = 0;

  for (int i=1; i<=k; i++) {
    ret += F_slow(n-i, k);
    ret %= MODULUS;
  }
  return ret;
}

long long F(int n, int k) {
  if (n < 0) return 0;
  if (n == 0) return 1;
  if (memo[n] != -1) return memo[n];

  long long ret = 0;
  
  if (n - k - 1 >= 0) {
    memo[n] = ((2 * F(n-1, k)) % MODULUS - F(n - k - 1, k));
    memo[n] %= MODULUS;
    memo[n] += MODULUS;
    memo[n] %= MODULUS;
    return memo[n];
  } else {
    return memo[n] = modexp(2, n-1);
    return memo[n] = F_slow(n, k);
  }
}

int main() {

  for (int i=0; i<MAX_N; i++) memo[i] = -1;

  for (int n=0; n<10; n++) {
    cout << "n=" << n << "\t" << F(n, 5) << endl;
    assert(F(n, 5) == F_slow(n, 5));
  }

  // return 0;

  cin >> N >> K;

  cout << F(N+1, K) << endl;

  return 0;
}
