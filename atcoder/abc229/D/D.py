#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

S = input()
K = read_int()

S = [1 if c == "." else 0 for c in S]
prefixes = [0]
for c in S:
    prefixes += [prefixes[-1] + c]

def min_delete(gap):
    ret = float("inf")
    for i in range(len(prefixes)+1):
        j = i + gap
        if j >= len(prefixes): break
        ret = min(ret, prefixes[j] - prefixes[i])
    return ret

def ok(r):
    return min_delete(r) <= K

def ans():
    low = 0
    assert(ok(low))
    high = len(S)+10
    assert(not ok(high))

    while high - low > 2:
        mid = (low + high) // 2
        if ok(mid):
            low = mid
        else:
            high = mid

    for r in range(low, low+10):
        if not ok(r):
            return r-1

print(ans())