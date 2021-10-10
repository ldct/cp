#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

"""
meet in the middle, meet-in-the-middle
"""
def subset_sums(arr, i, UB):
    if i == len(arr):
        return [0]
    ret = subset_sums(arr, i+1, UB)
    c = [r + arr[i] for r in ret]
    return [r for r in ret + c if r <= UB]

from collections import Counter

def freq(arr):
    return Counter(arr)

### CODE HERE

def ans(X, A):
    N = len(A)
    left = []
    right = []

    for i in range(len(A)):
        if i < (N//2):
            left += [A[i]]
        else:
            right += [A[i]]

    def ways(arr):
        ret = defaultdict(int)
        for a in subsets(arr):
            ret[sum(a)] += 1
        return ret

    left = freq(subset_sums(left, 0, X))
    right = freq(subset_sums(right, 0, X))

    ret = 0
    for k in left:
        ret += left[k]*right[X-k]
    return ret

if False:
    import random
    A = [random.randint(1, 10**9) for _ in range(40)]
    X = random.randint(1, 10**9)
    print(ans(X, A))
else:
    N, X = read_int_tuple()
    A = read_int_list()
    print(ans(X, A))