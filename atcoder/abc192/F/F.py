#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

if True:
    import random
    N = 100
    X = 10**17
    A = [random.randint(1, 10**7) for _ in range(N)]
    print(N, X)
    print(*A)
else:
    N, X = read_int_tuple()
    A = read_int_list()

from functools import lru_cache
from array import array

M = -1

n = N//2+1
memo = array('i', [-2]*N*N*(N+1))

def mc(i, target, c):
    # the sum of the subset of A[i:] with maximum sum whose sum is == target modulo

    # assert(M != -1)

    def rm(x):
        return ((x % M) + M) % M

    if i == 0 and c > N//2:
        r = rm(sum(A)-target)
        t = mc2(i, r, len(A) - c)
        if t == -1: return -1
        return sum(A) - t



    if c < 0: return -1

    if i == len(A):
        if target == 0 and c == 0: return 0
        return -1

    if c == 0:
        if target == 0: return 0
        return -1

    assert(0 <= i < N)
    assert(0 <= target < N)
    assert(0 <= c < n)

    if memo[i*N*N + target*N + c] != -2:
        return memo[i*N*N + target*N + c]

    option1 = mc(i+1, target, c)
    option2 = mc(i+1, rm(target - A[i]), c-1)

    if option2 != -1: option2 += A[i]

    if option1 == -1:
        memo[i*N*N + target*N + c] = option2
        return option2
    if option2 == -1:
        memo[i*N*N + target*N + c] = option1
        return option1

    memo[i*N*N + target*N + c] = max(option1, option2)
    return max(option1, option2)

memo2 = array('l', [-2]*N*N*(N+1))

def mc2(i, target, c):
    assert(M != -1)

    # the sum of the subset of A[i:] with maximum sum whose sum is == target modulo

    if c < 0: return -1

    if i == len(A):
        if target == 0 and c == 0: return 0
        return -1

    if c == 0:
        if target == 0: return 0
        return -1

    def rm(x):
        return ((x % M) + M) % M

    # assert(0 <= i < N)
    # assert(0 <= target < N)
    # assert(0 <= c <= N)

    if memo2[i*N*N + target*N + c] != -2:
        return memo2[i*N*N + target*N + c]

    option1 = mc2(i+1, target, c)
    option2 = mc2(i+1, rm(target - A[i]), c-1)

    if option2 != -1: option2 += A[i]

    if option1 == -1:
        memo2[i*N*N + target*N + c] = option2
        return option2
    if option2 == -1:
        memo2[i*N*N + target*N + c] = option1
        return option1

    memo2[i*N*N + target*N + c] = min(option1, option2)
    return min(option1, option2)

best = float("inf")

for t in range(1, N+1):
    M = t
    memo = array('l', [-2]*N*N*(N+1))
    memo2 = array('l', [-2]*N*N*(N+1))
    s = mc(0, X % t, t)
    # print(s)
    if s == -1: continue
    assert((X - s) % t == 0)
    best = min(best, (X - s) // t)

print(best)
