#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def cdiv(x, y):
    return x // y if x % y == 0 else x // y + 1

### CODE HERE

def ans3(K):
    ret = 0
    for a in range(1, K+1):
        for b in range(1, cdiv(K, a)+1):
            for c in range(1, cdiv(K, a*b)+1):
                if a*b*c <= K:
                    ret += 1
    return ret

K = read_int()

print(ans3(K))