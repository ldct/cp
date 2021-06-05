#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import math

### CODE HERE

def ans(lst):
    evens = []
    odds = []
    for a in lst:
        if a % 2 == 0:
            evens += [a]
        else:
            odds += [a]

    lst = evens + odds

    ret = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if math.gcd(lst[i], 2*lst[j]) > 1:
                ret += 1
    return ret

for _ in range(read_int()):
    input()
    print(ans(read_int_list()))