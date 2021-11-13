#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(a, b, c):
    ret = abs(a + c - 2*b)
    ret %= 3
    return min(
        ret,
        abs(ret-3),
        abs(ret+3)
    )


for _ in range(read_int()):
    print(ans(*read_int_list()))