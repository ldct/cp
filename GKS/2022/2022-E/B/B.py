#!/usr/bin/env python3

from bisect import bisect
from sys import stdin, stdout
from typing import Counter

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def ans(R):
    SR = sorted(R)
    CR = Counter(R)

    ret = []

    for r in R:
        i = bisect(SR, 2*r) - 1

        if i >= 0:
            if SR[i] == r and CR[r] == 1:
                i -= 1
                if i >= 0:
                    ret += [SR[i]]
                else:
                    ret += [-1]
            else:
                ret += [SR[i]]
        else:
            ret += [-1]

    return " ".join(map(str, ret))


T = int(input())
for t in range(T):
    N = read_int()
    R = read_int_list()
    print("Case #" + str(t+1) + ": " + str(ans(R)))
