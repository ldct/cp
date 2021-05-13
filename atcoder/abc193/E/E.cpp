#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll euclid(ll a, ll b, ll &x, ll &y) {
	if (!b) return x = 1, y = 0, a;
	ll d = euclid(b, a % b, y, x);
	return y -= a/b * x, d;
}

ll crt(ll a, ll m, ll b, ll n) {
	if (n > m) swap(a, b), swap(m, n);
	ll x, y, g = euclid(m, n, x, y);
	assert((a - b) % g == 0); // else no solution
	x = (b - a) % n * x % n / g * m + a;
	return x < 0 ? x + m*n/g : x;
}

ll intersect(ll a, ll b, ll c, ll d) {
  // find r such that aZ + b cap cZ + d = lcm(a, c)Z + r
  if ((b - d) % gcd(a, c) != 0) return -1;
  return crt(b,a,d,c);
}

void ans(ll X, ll Y, ll P, ll Q) {
  auto L1 = 2*(X+Y);
  auto L2 = P+Q;

  ll ret = LLONG_MAX;
  for (int y=X; y<X+Y; y++) for (int p=P; p<P+Q; p++) {
    auto candidate = intersect(L1, y, L2, p);
    if (candidate > 0) ret = min(ret, candidate);
  }

  if (ret == LLONG_MAX) {
    cout << "infinity" << endl;
    return;
  }
  cout << ret << endl;
}

int main() {
  int T;
  cin >> T;
  while (T --> 0) {
    ll x,y,p,q;
    cin >> x >> y >> p >> q;
    ans(x,y,p,q);
  }
}
