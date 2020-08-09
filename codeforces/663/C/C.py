#!/usr/bin/env pypy3

MODULUS = 10**9+7

def fac(n):
    ret = 1
    for i in range(1,n+1):
        ret *= i
        ret %= MODULUS
    return ret

n = int(input())

total_perms = fac(n)
non_cyclic = pow(2, n-1, MODULUS)

r = total_perms - non_cyclic
r %= MODULUS
r += MODULUS
r %= MODULUS

print(r)
