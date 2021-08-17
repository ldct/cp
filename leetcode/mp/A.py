#!/usr/bin/env pypy3

MODULUS = 10**9+7

def minNonZeroProduct(p):
    ret = 1
    ret *= (2**p-1)
    ret %= MODULUS

    K = (2**p-2) // 2
    B = 2*(2**(p-1)-1)

    ret *= pow(B, K, MODULUS)
    ret %= MODULUS

    if ret == 0: return 1
    return ret

print(minNonZeroProduct(1))
print(minNonZeroProduct(2))
print(minNonZeroProduct(60))