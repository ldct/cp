#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from itertools import permutations
from math import gcd

def ans(A):
    N = len(A)
    MAX_A = max(A)+1
    cnt = [0]*MAX_A
    best_inc = [0]*MAX_A

    for a in A:
        cnt[a] += 1

    for i in range(MAX_A):
        best_inc[i] = cnt[i]*(i-1)

    for i in range(2, MAX_A):
        for j in range(2*i, MAX_A, i):
        #   // update i->j
            best_inc[j] = max(best_inc[j], cnt[j]*(j-1) + best_inc[i])

    return max(best_inc) + N

def score(arr):
    ret = 0
    curr = arr[0]
    ret += curr
    for a in arr[1:]:
        curr = gcd(curr, a)
        ret += curr
    return ret

def ans_slow(A):
    return max(score(p) for p in permutations(A))

if True:
    tc = [6, 1, 4]
    print(ans_slow(tc))
    print(ans(tc))

elif True:
    import random
    for _ in range(100):
        tc = [random.randint(1, 6) for _ in range(3)]
        if not (ans(tc) == ans_slow(tc)):
            print(tc)

# input()
# A = read_int_list()
# print(ans_slow(A))