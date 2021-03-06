#!/usr/bin/env python3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from functools import lru_cache

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

from collections import Counter

### CODE HERE

def p1_wins(A):
    if sum(A) == 0: return False
    if len(A) == 2: return A[0] != A[1]

    cA = Counter(A)
    for k in cA:
        if k > 0 and cA[k] % 2 == 1:
            return True
    return False

def ans_slow(A):
    ret = 0
    for k in range(1, max(A) + 1):
        A_k = [a // k for a in A]
        for i in range(len(A_k)):
            if A_k[i] > 0:
                next_A = list(A_k)
                next_A[i] -= 1
                if not p1_wins(tuple(next_A)):
                    # print("removing", k, "works", next_A)
                    ret += 1
    return ret

if True:
    input()
    A = read_int_tuple()
else:
    import random
    A = [random.randint(1,20) for _ in range(20)]

# print(A)
print(ans_slow(A))
# print(p1_wins.cache_info())