#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import Counter

### CODE HERE

def ans(s):
    freq = Counter(s)

    odds = []
    evens = []

    for c in freq:
        if freq[c] % 2 == 1:
            odds += [c]
        else:
            evens += [c]

    if len(odds) > 1: return "NO SOLUTION"

    ret = ""
    if len(odds) == 1:
        c = odds[0]
        ret = c * freq[c]

    for c in evens:
        f = freq[c] // 2
        ret = f*c + ret + f*c

    return ret

print(ans(input()))