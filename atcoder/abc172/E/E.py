#!/usr/bin/env python3

import math

MODULUS = 10**9 + 7

def make_nCr_mod(max_n=5 * 10**5 + 100, mod=10**9 + 7):
    fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
    fact[0] = 1
    for i in range(max_n):
        fact[i + 1] = fact[i] * (i + 1) % mod

    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(max_n)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    def nCr_mod(n, r):
        res = 1
        while n or r:
            a, b = n % mod, r % mod
            if a < b:
                return 0
            res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
            n //= mod
            r //= mod
        return res

    return nCr_mod

nCr_mod = make_nCr_mod()

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

memo = dict()

@bootstrap
def f(n, m):
    assert(m >= n)
    if n < 0 or m < 0:
        yield 0
    if n == 0 or m == 0:
        yield 1

    key = (n,m)

    if key in memo:
        yield memo[key]

    t1 = yield f(n-2, m-2)
    t2 = yield f(n-1, m-1)
    t3 = yield f(n-1, m-1)
    ret = (n-1)*(t1 + t2) + (m-n)*t3
    ret = ret % MODULUS

    memo[key] = ret

    yield ret

def ans(N, M):
    return nCr_mod(M, N)*(math.factorial(N) % MODULUS)*f(N,M) % MODULUS

N, M = input().split(' ')
N = int(N)
M = int(M)
print(ans(N, M))
