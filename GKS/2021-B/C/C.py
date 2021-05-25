#!/usr/bin/env pypy3

from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def isqrt(n):
    if n > 0:
        x = 1 << (n.bit_length() + 1 >> 1)
        while True:
            y = (x + n // x) >> 1
            if y >= x:
                return x
            x = y
    elif n == 0:
        return 0
    else:
        raise ValueError("square root not defined for negative numbers")

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

class MillerRabin:
    def __init__(self):
        self._known_primes = [2, 3]
        self._known_primes += [x for x in range(5, 1000, 2) if self.is_prime(x)]

    def is_prime(self, n, _precision_for_huge_n=16):
        def _try_composite(a, d, n, s):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2**i * d, n) == n-1:
                    return False
            return True # n  is definitely composite

        if n in self._known_primes:
            return True
        if any((n % p) == 0 for p in self._known_primes) or n in (0, 1):
            return False
        d, s = n - 1, 0
        while not d % 2:
            d, s = d >> 1, s + 1
        if n < 1373653:
            return not any(_try_composite(a, d, n, s) for a in (2, 3))
        if n < 25326001:
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
        if n < 2**64:
            return not any(_try_composite(a, d, n, s) for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022))

        # otherwise
        return not any(_try_composite(a, d, n, s)
                    for a in _known_primes[:_precision_for_huge_n])

mr = MillerRabin()

def memoize(function):
  memo = {}
  def wrapper(*args):
    if args in memo:
      return memo[args]
    else:
      rv = function(*args)
      memo[args] = rv
      return rv
  wrapper.cache_info = memo
  return wrapper

@memoize
def prev_prime(x):
    x -= 1
    while not mr.is_prime(x): x -= 1
    return x

@memoize
def next_prime(x):
    x += 1
    while not mr.is_prime(x): x += 1
    return x

import math

def ans(Z):
    if isqrt(Z) == 2:
        p, q = 2, 3
    else:
        q = prev_prime(isqrt(Z))
        p = next_prime(q)

    while p*q <= Z:
        p, q = q, next_prime(q)

    while p*q > Z:
        p, q = prev_prime(p), p


    return p*q

if True:
    for Z in range(10**10, 10**10+10**6):
        ans(Z)
else:
    T = int(input())
    for t in range(T):
        N = read_int()
        print("Case #" + str(t+1) + ": " + str(ans(N)))
