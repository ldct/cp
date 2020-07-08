#include <bits/stdc++.h>

using namespace std;

template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }

constexpr int MODULUS = 998244353;

long long modpow(long long b, long long e) {
	long long ans = 1;
	for (; e; b = b * b % MODULUS, e /= 2)
		if (e & 1) ans = ans * b % MODULUS;
	return ans;
}

vector<int> A;

int N, M;

void query_one(int l, int r, int x) {
  for (int i=l; i<=r; i++) {
    A[i] = modpow(A[i], x);
  }
  return;
}

void query_two(int l, int r, int y) {
  long long mul_by = A[y];
  for (int i=l; i<=r; i++) {
    A[i] = (mul_by * A[i]) % MODULUS;
  }
  return;
}

void query_three(int z) {
  cout << A[z] << endl;
}

int main() {
  
  cin >> N >> M;

  for (int i=0; i<N; i++) {
    int a;
    cin >> a;
    A.push_back(a);
  }

  // cout << "A=" << A << endl;

  for (int i=0; i<M; i++) {
    int query_type;
    cin >> query_type;

    if (query_type == 1) {
      int l, r, x;
      cin >> l >> r >> x;
      query_one(l-1, r-1, x);
    } else if (query_type == 2) {
      int l, r, y;
      cin >> l >> r >> y;
      query_two(l-1, r-1, y-1);
    } else if (query_type == 3) {
      int z;
      cin >> z;
      query_three(z-1);
    }
    // cout << "A=" << A << endl;
  }

  return 0;
}
