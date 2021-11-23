#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def intersects(a, b):
    (i, j) = a
    (k, l) = b
    if j < k: return False
    if i > l: return False
    return True

def mi(p, q):
    a, b = p
    c, d = q
    a, b, c, d = sorted([a, b, c, d])
    return (b, c)

def dedup(arr):
    assert(len(arr) <= 3)
    if len(arr) == 1: return arr
    if len(arr) == 2:
        p, q = arr
        if intersects(p, q): return [mi(p, q)]
        return arr
    if len(arr) == 3:
        p, q, r = arr
        if intersects(p, q): return dedup([mi(p, q), r])
        if intersects(q, r): return dedup([mi(q, r), p])
        if intersects(p, r): return dedup([mi(p, r), q])
        arr = sorted(arr)
        return [arr[0], arr[-1]]

def merge(arr, r):
    return dedup(arr + [r])

data = [read_int_tuple() for _ in range(read_int())]

def ans(p):
    if len(p) == 1: return 0
    assert(not intersects(p[0], p[1]))
    a, b, c, d = sorted(p[0] + p[1])
    x = (b + c) // 2
    return max(x-b, c-x)

p = [data[0]]
print(ans(p))
for q in data[1:]:
    p = merge(p, q)
    print(ans(p))