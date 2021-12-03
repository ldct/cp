#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(a, b, c):
    total = a + 2*b + 3*c
    if total % 2 == 1:
        return "NO"

    # pair ca
    pairs = min(a, c)
    a -= pairs
    c -= pairs
    if c > 0: return "NO"

    # a must pair with itself or c
    if a % 2 == 1: return "NO"

    # get rid of b
    if b % 2 == 1 and pairs == 0:
        if a >= 2:
            a -= 2
        else:
            return "NO"

    return "YES"



    return a, b, c

for _ in range(read_int()):
    print(ans(*read_int_tuple()))