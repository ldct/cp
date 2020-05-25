#!/usr/bin/env python3
import math

T = int(input())

def num_diffs(m, a, b):
    ans = 0
    for i in range(m):
        if a[i] != b[i]: ans += 1
    return ans

def meld(m, a, b):
    idx = []
    for i in range(m):
        if a[i] != b[i]: idx += [i]
    
    [i, j] = idx

    first = list(a)
    second = list(a)

    first[i] = b[i]
    second[j] = b[j]

    return [''.join(first), ''.join(second)]

def ok(m, c, arr):
    for target in arr:
        if num_diffs(m, c, target) > 1: return False
    return True

def ans(n, m, arr):
    arr = list(set(arr))
    if len(arr) == 1:
        return arr[0]

    candidate = arr[0]

    for target in arr[1:]:
        if num_diffs(m, candidate, target) > 2: return -1
        if num_diffs(m, candidate, target) == 2:
            for c in meld(m, candidate, target):
                if ok(m, c, arr): return c
            return -1
    return candidate



    return '?'

# import random

# def random_string(m):
#     return ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(m))

# def testcase(n, m):
#     return [random_string(m) for _ in range(n)]

# def random_testcase():
#     n = random.randint(1, 10)
#     m = random.randint(1, 10)
#     return (n, m, testcase(n, m))

# for _ in range(10):
#     n, m, arr = random_testcase()
#     print(ans(n, m, arr))

for t in range(T):
    n, m = input().split(' ')
    n, m = int(n), int(m)

    arr = []
    for i in range(n):
        arr += [input()]
    
    print(ans(n, m, arr))