#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

MODULUS = 10**9 + 7


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


def _modinv(a, m):
    """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
    g, x, _ = extended_gcd(a % m, m)
    return x % m if g == 1 else None

INV_106 = _modinv(10**6, MODULUS)

def inv(a):
    if a == 10**6: return INV_106
    return _modinv(a, MODULUS)

class ModFrac():
    def __init__(self, a, b):
        self.val = (a * inv(b)) % MODULUS
        # self.a = a
        # self.b = b
        # self.check = a / b

    def __add__(self, rhs):
        if isinstance(rhs, int):
            return self + ModFrac(rhs, 1)
        r = ModFrac(1, 1)
        r.val = (self.val + rhs.val) % MODULUS
        return r

        # return ModFrac(
        #     self.a * rhs.b + rhs.a * self.b,
        #     self.b * rhs.b
        # )

    def __mul__(self, rhs):
        if isinstance(rhs, int):
            r = ModFrac(1, 1)
            r.val = (self.val * rhs) % MODULUS
            return r
            # return ModFrac(
            #     self.a * rhs, self.b
            # )
        r = ModFrac(1, 1)
        r.val = (self.val * rhs.val) % MODULUS
        return r
        # return ModFrac(
        #     self.a * rhs.a,
        #     self.b * rhs.b
        # )

    def __repr__(self):
        return f"{self.val}"

def ans(N, parent, queries):
    def ancestors(u):
        ret = []
        while u != 0:
            ret += [u]
            u = parent[u][0]
        return ret + [0]

    def P_occurs(u):
        if u == 0: return ModFrac(1, 1)
        p, a, b = parent[u]
        p_parent = P_occurs(p)
        return p_parent*a + (p_parent*(-1) + 1)*b

    # P(u | v)
    def P_occurs_cond(u, v):
        if u == v: return ModFrac(1, 1)
        p, a, b = parent[u]
        p_parent = P_occurs_cond(p, v)
        return p_parent*a + (p_parent*(-1) + 1)*b

    # P(u | !v)
    def P_occurs_cond_inv(u, v):
        if u == v: return ModFrac(0, 1)
        p, a, b = parent[u]
        p_parent = P_occurs_cond_inv(p, v)
        return p_parent*a + (p_parent*(-1) + 1)*b

    def lca(u, v):
        av = set(ancestors(v))
        for a in ancestors(u):
            if a in av: return a
        assert(False)

    ret = []
    for u, v in queries:
        if v in ancestors(u):
            ret += [P_occurs(v) * P_occurs_cond(u, v)]
        elif u in ancestors(v):
            ret += [P_occurs(u) * P_occurs_cond(v, u)]
        else:
            l = lca(u, v)
            p_l = P_occurs(l)
            ret += [
                p_l*P_occurs_cond(u, l)*P_occurs_cond(v, l) +
                (p_l*(-1) + 1) * P_occurs_cond_inv(u, l)*P_occurs_cond_inv(v, l)
            ]
    return ' '.join(map(str, ret))
    return ret

T = int(input())
for t in range(T):
    parent = dict()
    N, Q = read_int_tuple()
    K = read_int()
    parent[1] = (0, ModFrac(K, 10**6), 0)
    for i in range(N-1):
        p, a, b = read_int_tuple()
        parent[i+2] = (p, ModFrac(a, 10**6), ModFrac(b, 10**6))

    queries = []
    for _ in range(Q):
        queries += [read_int_tuple()]

    print("Case #" + str(t+1) + ": " + str(ans(N, parent, queries)))