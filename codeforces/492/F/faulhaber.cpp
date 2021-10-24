#include <bits/stdc++.h>
using namespace std;

constexpr int MODULUS = 1000000007;

long long modinv(int a, int b) {
	int b0 = b, t, q;
	int x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}

vector<long long> poly_mul(vector<long long>& a, vector<long long>& b) {
  vector<long long> ret(a.size()+b.size()-1, 0);
  for (int i=0; i<a.size(); i++) for (int j=0; j<b.size(); j++) {
    ret[i+j] += a[i]*b[j];
    ret[i+j] %= MODULUS;
  }
  return ret;
}

long long FT2[3009][3009];

void ft2(int m) {
  FT2[0][0] = 1;
  for (int i=1; i<=m; i++) {
    auto row = vector<long long>(i+1, 0);
    FT2[i][0] = 1;
    for (int j=1; j<i+1; j++) {
      FT2[i][j] = (FT2[i-1][j-1]) * i;
      FT2[i][j] %= MODULUS;
      FT2[i][j] *= (modinv(j+1, MODULUS) % MODULUS);
      FT2[i][j] %= MODULUS;

      FT2[i][0] += MODULUS - FT2[i][j];
      FT2[i][0] %= MODULUS;
    }
  }
}

vector<vector<long long>> faulhaberTriangle(int m) {
  vector<vector<long long>> ret = {{1}};

  for (int i=1; i<=m; i++) {
    auto row = vector<long long>(i+1, 0);
    row[0] = 1;
    for (int j=1; j<row.size(); j++) {
      row[j] = (ret[ret.size()-1][j-1]) * i;
      row[j] %= MODULUS;
      row[j] *= (modinv(j+1, MODULUS) % MODULUS);
      row[j] %= MODULUS;

      row[0] += MODULUS - row[j];
      row[0] %= MODULUS;
    }
    ret.push_back(row);
  }

  return ret;
}

long long N, D;

vector<int> children[3009];

vector<vector<long long>> FT;

void poly_sum_int(vector<__int128>& __restrict__ a, long long k, int e) {
  // a += integrate k*x^e
  for (int j=0; j<e+1; j++) {
    a[j+1] += (FT2[e][j]*k);
  }
}

vector<long long> integrate(vector<long long>& arr) {
  cout << "integrate" << arr.size() << endl;
  vector<__int128> ret(arr.size()+1,0);
  for (int i=0; i<arr.size(); i++) {
    for (int j=0; j<i+1; j++) {
      ret[j+1] += (FT2[i][j]*arr[i]);
    }
  }
  vector<long long> ret2;
  for (int i=0; i<ret.size(); i++) ret2.push_back(ret[i] % MODULUS); // ret[i] %= MODULUS;
  return ret2;
}

vector<long long> poly_of(int u) {
  vector<long long> ret = {1};
  for (auto v : children[u]) {
    auto tmp = poly_of(v);
    ret = poly_mul(ret, tmp);
  }
  return integrate(ret);
}

long long modexp(long long b, long long e) {
	long long ans = 1;
	for (; e; b = b * b % MODULUS, e /= 2)
		if (e & 1) ans = ans * b % MODULUS;
	return ans;
}

long long poly_eval(vector<long long>& p, int x) {
  long long ret = 0;
  for (int i=0; i<p.size(); i++) {
    ret += p[i]*modexp(x, i);
    ret %= MODULUS;
  }
  return ret;
}

int main() {

  cin >> N >> D;

  for (int i=0; i<N-1; i++) {
    int p;
    cin >> p;
    p --;
    children[p].push_back(i+1);
  }

  ft2(N+1);

  auto tmp = poly_of(0);

  cout << poly_eval(tmp, D) << endl;

  return 0;
}
