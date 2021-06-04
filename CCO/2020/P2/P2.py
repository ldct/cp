#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(B):
    A = list(range(1, len(B) + 1))

    T = len(A)-1
    def rightmost(A, B):
        nonlocal T
        for j in range(T, -1, -1):
            if B[j] < A[j]:
                T = j
                return T

    U = len(A)
    def leftmost(A, i, cap):
        nonlocal U
        U = min(U, i)
        for k in range(U, -1, -1):
            if A[k] <= cap:
                return k

    ret = 0

    while True:
        # print(A, B, T)

        j = rightmost(A, B)
        if j is None: return ret

        i = leftmost(A, j, B[j])
        if i is None: return -1

        del A[i]
        ret += (j-i)

        T -= 1

    return ret

input()
B = read_int_list()
print(ans(B))
