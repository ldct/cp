#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(A):
    ret = 0
    A = [(a,i+1) for i,a in enumerate(A)]
    A = sorted(A)[::-1]
    l = -1
    r = 1
    loc = [0]*(len(A)+1)
    for a, idx in A:
        if abs(l) == abs(r):
            # build at l
            loc[idx] = l
            ret += 2*abs(l)*a
            l -= 1
        else:
            loc[idx] = r
            ret += 2*abs(r)*a
            r += 1
    print(ret)
    print(*loc)

for _ in range(read_int()):
    input()
    A = read_int_list()
    ans(A)