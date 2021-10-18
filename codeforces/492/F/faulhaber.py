#!/usr/bin/env pypy3

# extended euclid
def egcd(a, b):
    """
    returns
    gcd(a, b), s, r
    s.t.
    a * s + b * r == gcd(a, b)
    """
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0


def modinv(a, m):
    """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
    g, x, _ = egcd(a % m, m)
    return x % m if g == 1 else None

from itertools import (accumulate, chain, count, islice, starmap)

def faulhaberTriangle_slow(m, p = 10**9+7):

    def Fraction(a, b):
        return (a * modinv(b, p)) % p

    '''List of rows of Faulhaber fractions.'''
    def go(rs, n):
        xs = list(starmap(
            lambda x, y: Fraction(n, x) * y,
            zip(islice(count(2), m), rs)
        ))
        return [Fraction(1 - sum(xs), 1)] + xs
    return list(map(lambda x : [r % p for r in x], list(accumulate(
        [[]] + list(islice(count(0), 1 + m)),
        go
    ))[1:]))

def faulhaberTriangle(m, p = 10**9+7):
    ret = [[1]]
    for i in range(1, m+1):
        row = [0]*(i+1)

        row[0] = 1
        for j in range(1, len(row)):
            row[j] = (ret[-1][j-1] * i * modinv(j+1, p)) % p
            row[0] -= row[j]
            row[0] %= p

        ret += [row]
    return ret
