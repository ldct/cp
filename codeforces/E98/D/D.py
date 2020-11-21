#!/usr/bin/env pypy3

import math

def extended_gcd(a, b):
    """returns gcd(a, b), s, r s.t. a * s + b * r == gcd(a, b)"""
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0


def modinv(a, m):
    """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
    g, x, _ = extended_gcd(a % m, m)
    return x % m if g == 1 else None

from fractions import Fraction

def Pok(n):
	if n < 0: return 0
	if n == 0: return 1

	ret = 0

	f = Fraction(1,2)
	x = n-1

	while x >= 0:
		ret += f*Pok(x)
		x -= 2
		f *= Fraction(1, 4)

	return ret

P = 998244353

def fib(n):
	a, b = 1, 1
	for _ in range(n-1):
		a, b = b, a+b
		a %= P
		b %= P

	return a

def ans(i):
	ret = fib(i) * modinv(pow(2, i, P), P)
	ret %= P
	ret += P
	ret %= P
	return ret

print(ans(int(input())))
