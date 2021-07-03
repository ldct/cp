#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(A, B, C, D):
    if B >= D*C:
        return -1
    ret = 0
    a = A
    b = 0
    while a > D*b:
        a += B
        b += C
        ret += 1
    return ret

print(ans(*read_int_list()))