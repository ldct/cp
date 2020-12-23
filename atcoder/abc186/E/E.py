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

def ans(N, S, K):
    # find the smallest x >= 0 s.t.
    # Kx = -S mod N

    S = N - S
    S %= N
    S += N
    S %= N

    # the equation is now
    # Kx = S mod N

    d = math.gcd(K, N)
    if S % d != 0: return -1

    K //= d
    S //= d
    N //= d

    # the equation is now
    # Kx = S mod N
    # where K, N are coprime

    ret = S*modinv(K, N)
    ret %= N
    ret += N
    ret %= N

    return ret


for _ in range(int(input())):
    [N, S, K] = list(map(int, input().split()))
    print(ans(N, S, K))