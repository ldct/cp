#!/usr/bin/env python3

import sys
sys.setrecursionlimit(5000)

from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

MODULUS = 10**9+7

ALPHABET_SIZE = 26

K = int(input())
S = input()

from functools import lru_cache

def choose(n,k,p):
    if k > n:
        return 0

    # calculate numerator
    num = 1
    for i in range(n,n-k,-1):
        num = (num*i)%p

    # calculate denominator
    denom = 1
    for i in range(1,k+1):
        denom = (denom*i)%p

    # numerator * denominator^(p-2) (mod p)
    return (num * pow(denom,p-2,p))%p

memo = dict()

@bootstrap
def f(s, k):
    if s == 0:
        yield (ALPHABET_SIZE**k % MODULUS)
    if s < 0:
        return (ALPHABET_SIZE)**(k+s)
    if k == 0:
        yield 1
    if k < 0:
        yield 0

    if (s, k) in memo: yield memo[(s, k)]

    ret = 0

    for i in range(0, s+1):
        m = choose(s, i, MODULUS)*pow(ALPHABET_SIZE-1,s-i,MODULUS) % MODULUS
        ret += m*(yield f(s, -s)) % MODULUS

    memo[(s, k)] = ret

    yield ret

print(f(len(S), K))