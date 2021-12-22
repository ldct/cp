#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

def merge_list(left,right):
    result = list()
    i,j = 0,0
    inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv_count += (len(left)-i)
    result += left[i:]
    result += right[j:]
    return result,inv_count


def sort_and_count(array):
    if len(array) <= 1:
        return array, 0
    middle = len(array) // 2
    left,inv_left = sort_and_count(array[:middle])
    right,inv_right = sort_and_count(array[middle:])
    merged, count = merge_list(left,right)
    count += (inv_left + inv_right)
    return merged, count


def count_inversions(arr):
    _, ret = sort_and_count(arr[:])
    return ret

### CODE HERE

def weak(B):
    ret = 0
    for i in range(len(B)):
        for j in range(i+1, len(B)):
            if B[i] <= B[j]: ret += 1
    return ret

def ans_slow(A, B):
    ret = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] >= A[j] and B[i] <= B[j]:
                # print(i, j)
                ret += 1
    return ret

def ans(A, B):
    pairs = []
    for i in range(len(A)):
        a, b = A[i], B[i]
        pairs += [(-a, b)]
    pairs.sort()
    B = [p[1] for p in pairs]
    N = len(A)

    cp = Counter(pairs)

    ret = 0
    for k in cp:
        v = cp[k]
        if v == 1: continue
        ret += (v*(v-1))//2


    return ret + N + N*(N-1)//2 - count_inversions(B)


if False:
    import random
    N = 2*10**5
    A = [random.randint(1, 10**5) for _ in range(N)]
    B = [random.randint(1, 10**5) for _ in range(N)]
    print(ans(A, B))
elif False:
    import random

    for N in range(1, 10):
        print(N)
        for _ in range(1000):
            B = [random.randint(1, 2*N) for _ in range(N)]
            assert(weak(B) == N*(N-1)//2 - count_inversions([b for b in B]))
elif False:

    import random

    for N in range(1, 100):
        print(N)
        for _ in range(1000):
            A = [random.randint(1, 2*N) for _ in range(N)]
            B = [random.randint(1, 2*N) for _ in range(N)]
            assert(ans(A, B) == ans_slow(A, B))
else:
    input()
    A, B = read_int_list(), read_int_list()
    print(ans(A, B))
