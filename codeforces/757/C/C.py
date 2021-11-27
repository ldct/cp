#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

MODULUS = 1000000007

def or_elems(arr):
    assert(len(arr) > 0)
    ret = arr[0]
    for a in arr[1:]:
        ret |= a
    return ret

def coziness(nums):
    bits = 0
    for a in nums:
        bits |= a
    return bits * int(pow(2, len(nums)-1, MODULUS))

MAX_BIT = 32
def ans(N, constraints):
    big_arr = [0]*(N)
    constraints = [(l-1, r-1, x) for l,r,x in constraints]
    for b in range(MAX_BIT):
        paint = [0]*(N+1)
        for l,r,x in constraints:
            if (x & (1 << b)) == 0:
                paint[l] += 1
                paint[r+1] -= 1
        arr = [0]
        for p in paint:
            arr += [arr[-1] + p]
        arr = arr[1:-1]
        arr = [1 if x == 0 else 0 for x in arr]
        for i in range(N):
            big_arr[i] += arr[i]*(1 << b)

    print(big_arr)

    return coziness(big_arr) % (10**9+7)

for _ in range(read_int()):
    N, M = read_int_tuple()
    constraints = [read_int_tuple() for _ in range(M)]
    print(ans(N, constraints))
