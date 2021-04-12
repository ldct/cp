#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

input()
S = input()
A = read_int_list()

def ok_A(A):
    for a in A:
        if a < 0:
            return False
    for i in range(len(S)):
        if S[i] == '<':
            if A[i] >= A[i+1]: return False
        if S[i] == '>':
            if A[i] <= A[i+1]: return False
    return True

from functools import lru_cache

@lru_cache(None)
def ok_k(k):
    ret = []
    for _ in range(k):
        ret.append([])
    for a in A:
        for r in ret:
            r.append(a // k)
        excess = a - (a // k)*k
        assert(excess < k)
        for i in range(excess):
            ret[i][-1] += 1
    for r in ret:
        if not ok_A(r):
            return False
    return ret

low = 1
high = max(A)+1

assert(ok_k(low))
assert(not ok_k(high))

while high - low > 3:
    mid = (low + high) // 2
    if ok_k(mid):
        low = mid
    else:
        high = mid

for k in range(low, low+10):
    r = ok_k(k)
    if r == False:
        print(k-1)
        for p in ok_k(k-1):
            print(*p)
        break
