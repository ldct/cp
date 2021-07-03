#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

MODULUS = 998244353

import math

def modFact(n, p=MODULUS):
    if n >= p:
        return 0

    result = 1
    for i in range(1, n + 1):
        result = (result * i) % p

    return result

def extended_gcd(a, b):
    """returns gcd(a, b), s, r s.t. a * s + b * r == gcd(a, b)"""
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0


def modinv(a, m=MODULUS):
    """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
    g, x, _ = extended_gcd(a % m, m)
    return x % m if g == 1 else None

def ncr(N, K):
    # compute n choose k in O(k) time
    ret = 1
    for i in range(1, K+1):
        ret *= (N - K + i)
        ret *= modinv(i)
        ret %= MODULUS
    return ret

# number of compositions of N into exactly K parts
def comp(N, K):
    ret = (ncr(N-1, K-1)) % MODULUS
    return ret

def f(N, K):
    if K == 0: return 0
    return (pow(K, N) - K*f(N, K-1)) % MODULUS

def ans(N, K):
    N -= 1
    K -= 1
    if K == 0: return 0

    ret = 1
    ret *= (K+1) # choose the first colour
    ret *= f(N, K)
    ret %= MODULUS
    return ret

N, K = read_int_tuple()

print(ans(N, K))