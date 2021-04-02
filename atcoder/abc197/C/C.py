#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def p_score(p):
    ret = 0
    for n in p:
        ret |= n
    return ret

def ans(A):
    def vals(arr):
        if len(arr) == 1:
            return set([arr[0]])
        ret = set()
        ret.add(p_score(arr))
        for i in range(1, len(arr)):
            for c in vals(arr[i:]):
                ret.add(p_score(arr[:i]) ^ c)
        return ret

    candidates = []
    for c in vals(A):
        candidates += [c]

    return min(candidates)

if False:
    import random, sys
    for _ in range(1):
        tc = [random.randint(0, 10) for _ in range(20)]
        print(tc, ans(tc))
else:
    input()
    A = read_int_list()
    print(ans(A))
