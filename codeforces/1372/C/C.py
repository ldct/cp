#!/usr/bin/env pypy3

def is_sorted(A):
    for i, a in enumerate(A):
        if i+A[0] != a: return False
    return True

def ok_1(A):
    i = 0
    while i < len(A) and i+1 == A[i]:
        i += 1
    while i < len(A) and i+1 != A[i]:
        i += 1
    return is_sorted(A[i:])

def ans(A):
    if is_sorted(A):
        return 0
    if ok_1(A):
        return 1
    return 2

T = int(input())

for t in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    print(ans(A))