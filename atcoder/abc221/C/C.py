#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import chain, combinations

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

### CODE HERE

def extract(s, N):
    ret = ""
    for i in s:
        ret += N[i]
    ret = ''.join(sorted(ret)[::-1])
    if ret[0] == "0": return 0
    return int(ret)

def ans(N):
    ret = -1
    for left in subsets(range(len(N))):
        left = set(left)
        right = set(range(len(N))) - left
        if len(left) == 0: continue
        if len(right) == 0: continue
        ret = max(ret, extract(left, N)*extract(right, N))
    return ret

N = input()
print(ans(N))