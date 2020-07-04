#!/usr/bin/env python3

from collections import deque

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def descendents(A):
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            A1 = A[:]
            A2 = A[:]

            del A1[i]
            del A2[i+1]

            return [A1, A2]
    return []

def ans_slow(A):
    work = deque([A])

    while len(work):
        A = work.popleft()
        if len(A) == 1:
            return "YES"
        for B in descendents(A):
            work.append(B)

    return "NO"    

def ans(A):
    one_idx = A.index(1)
    if one_idx == len(A)-1:
        if A[0] == 1: return "YES"
        return "NO"
    right_max = A[-1]
    if right_max > A[0]: return "YES"
    return "NO"

# from itertools import permutations

# for p in permutations(range(1,7)):
#     if ans(list(p)) != ans_slow(list(p)):
#         print(p, ans(list(p)))

T = int(input())

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    print(ans(A))