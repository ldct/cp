#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

import math

def ans(n, k):
    if n % k == 0: return 1
    if k == n: return 1
    if k < n: return 2
    if k % n > 0:
        k += (n - k%n)
    return k // n

def ans_slow(n, k):
    for i in range(n, 1000000000):
        if i % k == 0:
            while i % n != 0:
                i += 1
            return i // n

for _ in range(read_int()):
    print(ans(*read_int_tuple()))