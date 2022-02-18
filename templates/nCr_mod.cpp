// computes n choose k modulo a prime by precomputing all the factorials

int factorial[5009];
int finv[5009];

int modinv(int a, int b) {
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

int nCr_mod(int n, int k) {
  if (k == 0) return 1;
  if (k == 1) return n;
  if (n == k) return 1;
  auto ret = factorial[n] * finv[k] % MODULUS * finv[n - k] % MODULUS;
  return ret;
}

i32 main() {
  factorial[0] = 1;
  for (int i = 1; i <= 5000; i++) {
      factorial[i] = factorial[i - 1] * i % MODULUS;
      finv[i] = modinv(factorial[i], MODULUS);
  }
  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS