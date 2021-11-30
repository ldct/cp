#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

import math

class Sieve:
    def __init__(self, n=10**6+100):
        self.N = n

        s = [-1] * n
        for i in range(2, int(n**0.5)+1):
            if s[i] != -1: continue
            for j in range(i, n, i):
                if j > i: s[j] = i
        self.s = s

    def isprime(self, n):
        if n in [0,1]: return False
        if n < self.N:
            return self.s[n] == -1

sieve = Sieve()

def prod(arr):
    ret = 1
    for a in arr: ret *= a
    return ret

def ans_block_slow(arr):
    ret = 0
    for i in range(len(arr)+1):
        for j in range(i+2, len(arr)+1):
            if sieve.isprime(prod(arr[i:j])):
                ret += 1
    return ret

def ans_block(arr):
    sizes = [0]
    for a in arr:
        if a == 1:
            sizes[-1] += 1
        else:
            sizes += [0]
    ret = 0
    for i in range(len(sizes)-1):
        a, b = sizes[i], sizes[i+1]
        ret += (a+1)*(b+1) - 1
    return ret


if False:
    import random
    for N in range(1, 10):
        for _ in range(100000):
            tc = [random.choice([1,3]) for _ in range(N)]
            assert(ans_block(tc) == ans_block_slow(tc))
        print("done", N)

def ans_adj(arr):
    arrs = [[]]
    for a in arr:
        if sieve.isprime(a) or a == 1:
            arrs[-1] += [a]
        else:
            if len(arrs[-1]):
                arrs += [[]]

    ret = 0
    for arr in arrs:
        ret += ans_block(arr)
    return ret

def ans(e, A):
    arrs = []
    for _ in range(e):
        arrs += [[]]

    for i in range(len(A)):
        arrs[i % e] += [A[i]]

    ret = 0
    for arr in arrs:
        ret += ans_adj(arr)
    return ret

for _ in range(read_int()):
    N, E = read_int_tuple()
    A = read_int_list()
    print(ans(E, A))