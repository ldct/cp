#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from collections import Counter
def ans(A):
    target = 2*sum(A)
    N = len(A)
    if target % N != 0: return 0
    target = target // N

    freq = Counter(A)
    elems = set(A)

    ret = 0
    for e in elems:
        f = target - e
        if e > f: continue
        if e == f:
            ret += freq[e] * (freq[e]-1) // 2
        else:
            ret += freq[e]*freq[f]
    return ret

    return A, target, freq

for _ in range(read_int()):
    input()
    A = read_int_list()
    print(ans(A))