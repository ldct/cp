#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from heapq import *

def ans(N, X, Y):
    total = (N+1)*N // 2

    if (total % (X+Y)) > 0:
        print("IMPOSSIBLE")
        return

    print("POSSIBLE")

    ret = []
    heap = []
    for e in range(1, N+1):
        heappush(heap, -e)

    target = total*X // (X+Y)
    old_target = target

    while len(heap):
        top = -heappop(heap)

        if top <= target:
            target -= top
            ret += [top]

    print(len(ret))
    print(*ret)

T = int(input())
for t in range(T):
    N, X, Y = read_int_tuple()
    print("Case #" + str(t+1) + ": ", end='')
    ans(N, X, Y)
