#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE


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

MODULUS = 998244353
INV_2 = pow(2, MODULUS-2, MODULUS)
INV_10 = pow(10, MODULUS-2, MODULUS)
B_SUB_INV = modinv(2*INV_10-1, MODULUS)

def w(x):
    if x == 0: return 0
    return x-1

def ans_triplet(S):
    ret = 0
    N = len(S)
    for i in range(N+1):
        for k in range(i+1, N+1):
            for j in range(i, k):
                ret += int(S[j])*pow(10, k-j-1, MODULUS)*pow(2, w(i)+w(N-k), MODULUS)
                ret %= MODULUS
    return ret

def p(b, e):
    return pow(b, e, MODULUS)

def dsum(j, N):
    b = 2*INV_10
    ret = p(2,j)-1
    ret *= B_SUB_INV*INV_2*(p(b, N-j) - b)
    ret += (p(b, N-j) - b)*B_SUB_INV*INV_2*p(2, 0)
    ret += (p(2,j)-1)
    ret += 1

    return ret*INV_10*p(10, N)*p(INV_10, j)
"""
k=j+1 k=N
t=N-j-1 t=0
t = N-k

"""
def ans(S):
    ret = 0
    N = len(S)
    for j in range(N):
        sj = int(S[j])
        ret += dsum(j, N)*sj
        ret %= MODULUS
    return ret

for tc in range(1, 1):
    t = str(tc)
    assert(ans_triplet(t) == ans(t))

print(ans(input()))
