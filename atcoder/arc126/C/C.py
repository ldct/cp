#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, K = read_int_tuple()
A = read_int_list()

def cost1(a, m):
    if a % m == 0: return 0
    return m - (a % m)

def ok(g):
    return sum([cost1(a, g) for a in A]) <= K

low = 1
high = 10**20

assert(ok(low))
assert(not ok(high))

while high - low > 2:
    mid = (low + high) // 2
    if ok(mid):
        low = mid
    else:
        high = mid

for g in range(1, 100):
    print(g, ok(g))
    # if not ok(g):
    #     print(g-1)
    #     break