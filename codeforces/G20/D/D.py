#!/usr/bin/env pypy3

import io, os, sys
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

def indexes(A):
    ret = defaultdict(list)
    for i, a in enumerate(A):
        ret[a] += [i]
    return ret

def del_indexes(A, indexes):
    A = A[:]
    for i in indexes:
        A[i] = None
    return [a for a in A if a is not None]

def ans(A, B):

    A = A[::-1]
    B = B[::-1]

    reserve = defaultdict(int)

    i = 0
    j = 0

    while True:
        if j == len(A): return True
        if A[i] == B[j]:
            i += 1
            j += 1
            continue

        if 0 < j < len(B) and B[j] == B[j-1]:
            reserve[B[j]] += 1
            j += 1
            continue

        if i < j and reserve[A[i]] > 0:
            reserve[A[i]] -= 1
            i += 1
            continue

        return False



def squish(arr, i, j):
    arr = list(arr)
    arr.insert(j, arr[j])
    del arr[i]
    return tuple(arr)

def bfs(arr):
    visited = set([tuple(arr)])

    while True:
        next_visited = set()
        for arr in visited:
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    if arr[i] == arr[j]:
                        nxt = squish(arr, i, j)
                        if nxt not in visited:
                            next_visited.add(nxt)
        if len(next_visited) == 0: return visited

        for v in next_visited: visited.add(v)

def ans_slow(A, B):
    return tuple(B) in bfs(A)

if False:
    A, B = [2, 3, 2, 1, 2], [3, 2, 1, 2, 2]
    print(ans_slow(A, B))
    print(ans(A, B))
elif False:
    import random
    for _ in range(100000):
        A = [random.randint(1, 5) for _ in range(10)]
        B = A[:]
        random.shuffle(B)
        if not (ans(A, B) == ans_slow(A, B)):
            print(A, B)
            break
elif True:
    for _ in range(read_int()):
        input()
        A = read_int_list()
        B = read_int_list()
        print("YES" if ans(A, B) else "NO")