#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE


def pow2(A, B, C, MODULUS):
    A %= MODULUS
    if A == 0: return 0
    BC = pow(B, C, MODULUS-1)
    return pow(A, BC, MODULUS)

def pow2_slow(A, B, C, MODULUS):
    BC = pow(B, C)
    return pow(A, BC, MODULUS)

if False:
    for MODULUS in [3, 5, 7, 11, 13, 97]:
        print("checking", MODULUS)
        for A in range(10):
            for B in range(10):
                for C in range(10):
                    if not (pow2_slow(A, B, C, MODULUS) == pow2(A, B, C, MODULUS)):
                        print(A, B, C, MODULUS)
N, K, M = read_int_tuple()
print(pow2(M, K, N, 998244353))