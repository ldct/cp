#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

constexpr int MODULUS = 1000000007;

long long modexp(long long b, long long e) {
	long long ans = 1;
	for (; e; b = b * b % MODULUS, e /= 2)
		if (e & 1) ans = ans * b % MODULUS;
	return ans;
}

struct UF {
  vector<int> e;
  UF(int n) : e(n, -1) {}
  int components() {
    set<int> ret;
    for (int i=0; i<e.size(); i++) {
      int u = find(i);
      ret.insert(u);
    }
    return ret.size();
  }
  bool sameSet(int a, int b) { return find(a) == find(b); }
  int size(int x) { return -e[find(x)]; }
  int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
  bool join(int a, int b) {
    a = find(a), b = find(b);
    if (a == b) return false;
    if (e[a] > e[b]) swap(a, b);
    e[a] += e[b]; e[b] = a;
    return true;
  }
};

int K, P;

i32 main() {

  cin >> P >> K;

  auto uf = UF(P);

  for (int i=0; i<P; i++) {
    uf.join(i,(i*K) % P);
  }

  if (K == 0) {
    cout << modexp(P, P-1) << endl;
  } else if (K == 1) {
    cout << modexp(P, P) << endl;
  } else {
    cout << modexp(P, uf.components()-1) << endl;
  }


  return 0;
}
