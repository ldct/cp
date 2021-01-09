#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def is_hv(A, i):
    if not (0 <= i-1 < i+1 < len(A)): return False
    if A[i] > max(A[i-1], A[i+1]): return True
    if A[i] < min(A[i-1], A[i+1]): return True
    return False

def is_hill(A, i):
    if not (0 <= i-1 < i+1 < len(A)): return False
    if A[i] > max(A[i-1], A[i+1]): return True
    return False

def is_valley(A, i):
    if not (0 <= i-1 < i+1 < len(A)): return False
    if A[i] < min(A[i-1], A[i+1]): return True
    return False

def count_hv(A):
    ret = 0
    for i in range(len(A)):
        if is_hv(A, i):
            ret += 1
    return ret

def is_hv_cf(A, i, k, j):
    old = A[i]
    A[i] = k
    ret = is_hv(A, j)
    A[i] = old
    return ret

def decrease_two(A):
    for i in range(len(A)):
        if is_hv(A, i) and is_hv(A, i+1):
            if not is_hv_cf(A, i+1, A[i], i+2): return True
            if not is_hv_cf(A, i, A[i+1], i-1): return True
    return False

def decrease_three(A):
    for i in range(len(A)):
        if is_hv(A, i) and is_hv(A, i+1) and is_hv(A, i+2):
            return True
    return False

def ans(A):
    initial_hv = count_hv(A)

    if initial_hv in [0, 1]: return 0
    if decrease_three(A): return initial_hv - 3
    if decrease_two(A): return initial_hv - 2

    return initial_hv - 1

    return '?'

def ans_slow(A):
    ret = count_hv(A)
    for d in range(min(A), max(A)+1):
        for i in range(len(A)):
            new_A = A[:]
            new_A[i] = d
            ret = min(ret, count_hv(new_A))

    return ret

for _ in range(read_int()):
    input()
    A = read_int_list()
    print(ans(A))