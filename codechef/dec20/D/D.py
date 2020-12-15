#!/usr/bin/env pypy3

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

def frac(p, q, m):
    return (p*modinv(q, m)) % m

MODULUS = 998244353

def ans(N):
    if N == 1: return 1
    if N == 2: return frac(8,3,MODULUS)
    if N == 3: return frac(31,15,MODULUS)

print(ans(int(input())))