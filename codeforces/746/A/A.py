#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(H, A):
    A = sorted(A)[::-1]
    if A[0] >= H: return 1
    ret = 0
    double = A[0] + A[1]
    ret += 2*(H // double)
    H -= (H // double)*double
    assert(H>=0)
    if H <= 0: return ret

    ret += 1
    H -= A[0]
    if H <= 0: return ret

    ret += 1
    H -= A[1]
    if H <= 0: return ret


    return ret, H, A

for _ in range(read_int()):
    N, H = read_int_tuple()
    A = read_int_list()
    print(ans(H, A))