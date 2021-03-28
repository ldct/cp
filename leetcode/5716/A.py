#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

MODULUS = 10**9 + 7

def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def ans_fast(n):
    if n < 2: return ans(n)
    if n % 3 == 0:
        return pow(3, n // 3, MODULUS)
    elif n % 3 == 1:
        return (4*pow(3, (n // 3)-1, MODULUS)) % MODULUS
    else:
        return (2*pow(3, (n // 3), MODULUS)) % MODULUS

def ans(n):
    def ans_k(k):
        start = n
        ret = []
        while start > k:
            ret += [k]
            start -= k
        if start == 1:
            if len(ret):
                ret[0] += 1
            else:
                ret += [start]
        elif n > 1:
            ret += [start]
        return product(ret)

    return ans_k(3)

for n in range(1, 20):
    print(ans(n), ans_fast(n))