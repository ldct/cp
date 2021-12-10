#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict

### CODE HERE

def f(i):
    return 9*i*(10**(i-1))

def ans(k):
    k -= 1
    i = 1
    while f(i) <= k:
        k -= f(i)
        i += 1
    group = 10**(i-1) + k // i
    j = k % (len(str(group)))
    # print(group, j)
    return str(group)[j]

s = ""
for i in range(1, 1000):
    s += str(i)

def ans_slow(k):
    global s
    return s[k-1]

if False:
    k = 7
    print(ans_slow(k))
    print(ans(k))
elif False:
    for k in range(1, 100):
        if not (ans(k) == ans_slow(k)):
            print(k)
            break
else:
    for _ in range(read_int()):
        print(ans(read_int()))