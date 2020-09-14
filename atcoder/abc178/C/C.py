#!/usr/bin/env pypy3

MODULUS = 10**9+7

N = int(input())

ret = pow(10, N, MODULUS)
ret -= 2*pow(9, N, MODULUS)
ret += pow(8, N, MODULUS)

print((ret%MODULUS + MODULUS) % MODULUS)