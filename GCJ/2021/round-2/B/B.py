#!/usr/bin/env pypy

from __future__ import division, print_function

import itertools
import sys
import math

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import math

import math

def divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

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

def ans(N):
    ret = -1
    for n in range(1, N+1):
        ret = max(ret, deepest(n, N))
    return ret

def deepest_checked(N, budget):
    if budget < 0: return float("-inf")
    if budget == 0: return 0
    if budget % N != 0: return float("-inf")

    return deepest2(1, budget // N)

    # also can
    return (N, budget)

@memoize
def deepest2(N, budget):
    ret = float("-inf")

    for i in range(2, 10**6):
        if N*i > budget: break
        ret = max(ret, 1+deepest_checked(N*i, budget-N*i))

    return ret

def ans2(N):
    ret = -2
    for p in range(3, N+1):
        if N-p < 0: break
        old_ret = ret
        ret = max(ret, deepest_checked(p, N-p))
    return 1+ret

@memoize
def deepest(D, S):
    if D == S: return 1
    if D > S: return float("-inf")
    ret = float("-inf")

    for d in divisors(D):
        if d < 3: continue
        if d == D: continue
        ret = max(ret, 1+deepest(d, S-D))
    return ret

if False:
    import random
    tc = [random.randint(10**5, 10**6) for _ in range(100)]
    for t in tc: ans2(t)
    print(len(deepest2.cache_info))
else:
    T = int(input())
    for t in range(T):
        N = read_int()
        print("Case #" + str(t+1) + ": " + str(ans2(N)))
