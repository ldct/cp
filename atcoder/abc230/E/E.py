#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

import math

### CODE HERE

def ans_slow(N):
    return sum([math.floor(N / i) for i in range(1, N+1)])

def ans(N):
    prefix = []
    i = 1
    for _ in range(math.ceil(math.sqrt(N))):
        prefix += [N // i]
        i += 1
    d = dict()
    for k in prefix:
        d[k] = 1

    for i in range(len(prefix)-1):
        d[i+1] = prefix[i] - prefix[i+1]

    ret = 0
    for k in d:
        ret += k*d[k]
    return ret

print(ans(read_int()))