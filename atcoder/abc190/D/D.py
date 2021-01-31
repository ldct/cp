#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N = read_int()
N *= 2

ret = set()

def solve(p, q):
    q -= 1
    b2 = p + q
    if b2 % 2 == 1: return None
    b = b2 // 2
    a = p - b
    assert(b - a == q)
    return (a,b)

i = 1
while i*i <= N:
    if N % i != 0:
        i += 1
        continue

    for r in [solve(i, N//i), solve(N//i, i)]:
        if r is not None:
            ret.add(r)
    i += 1

print(len(ret))