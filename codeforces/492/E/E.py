#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import random, math

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

def fermat_isprime(n, k=100):
    if n == 2: return True
    if n % 2 == 0: return False

    for i in range(k):
        a = random.randint(1, n-1)

        if pow(a, n-1, n) != 1:
            return False
    return True

def random_prime():
    for _ in range(100):
        r = random.randint(10**8, 10**9)
        if fermat_isprime(r):
            return r
    assert(False)

def random_seq(u, p):
    for _ in range(100):
        r = random.choice([0,1,2])
        if r == 0:
            u += 1
        elif r == 1:
            u -= 1
        else:
            u = modinv(u, p)
        u %= p
    return u

def ans(u, v, p):
    u_end = set([random_seq(u, p) for _ in range(10**5)])
    v_end = set([random_seq(v, p) for _ in range(10**5)])

    print(len(u_end), len(v_end))

    for uu in u_end:
        vv = p - uu
        if vv in v_end:
            return True
    return False

def tc():
    p = random_prime()
    u = random.randint(1, p)
    v = random.randint(1, p)
    return (u, v, p)

print(*tc())

### CODE HERE

# for _ in range(read_int()):
#     pass