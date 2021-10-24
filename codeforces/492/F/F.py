#!/usr/bin/env pypy3

import sys
from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict
from functools import lru_cache

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

def sum_pows(k, n, p = 10**9+7):
    coefficients = faulhaberTriangle(k)[k-1]
    return sum(e*n**(i+1) for i, e in enumerate(coefficients)) % p

def poly_mul(A, B):
  ret = [0]*(len(A)+len(B)-1)
  for i, a in enumerate(A):
    for j, b in enumerate(B):
      ret[i+j] += a*b
      ret[i+j] %= 10**9+7
  return ret

def poly_sum(A, B):
  ret = [0]*max(len(A),len(B))

  for i in range(len(A)):
    ret[i] += A[i]
    ret[i] %= 10**9+7
  for j in range(len(B)):
    ret[j] += B[j]
    ret[j] %= 10**9+7


  return ret

def sum_pows_poly(k, n, p = 10**9+7):
    coefficients = faulhaberTriangle(k)[k-1]
    return [0] + coefficients

children = defaultdict(list)

n, D = read_int_tuple()
for i in range(n-1):
  p = read_int() - 1
  children[p] += [i+1]

FT = faulhaberTriangle(n+1)

def integrate_monic_monomial(i):
    # integrate x^i
    ret = FT[i]
    return [0] + ret

def integrate_monomial(k, i):
    # integrate kx^i
    return [k*r for r in integrate_monic_monomial(i)]

def integrate(arr):
    ret = []
    for i, a in enumerate(arr):
        ret = poly_sum(ret, integrate_monomial(a, i))
        # print("ret=", ret)
    return ret

def poly_of(u):
    # returns f: d -> f(d) in coefficient form
    # f(d) = sum_{u=1 ^ d} ( g_1(u) * g_2(u) * ... ) where g runs over the children

    ret = [1]
    for v in children[u]:
        ret = poly_mul(ret, poly_of(v))

    return integrate(ret)

def poly_eval(p, x, MODULUS=10**9+7):
    ret = 0
    for i, k in enumerate(p):
        ret += k*pow(x, i, MODULUS)
        ret %= MODULUS
    return ret

p = poly_of(0)
print(poly_eval(p, D))
