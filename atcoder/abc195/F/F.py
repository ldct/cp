#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import chain, combinations

from math import gcd

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

### CODE HERE

def ok(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if gcd(s[i], s[j]) > 1:
                return False
    return True

A, B = read_int_tuple()
elems = list(range(A, B+1))

ret = 2**len(elems)

for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]:
    r = 0
    for e in elems:
        if e % p == 0:
            r += 1
    ret -= 2**r

print(ret)