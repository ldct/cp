#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def score(S):
    ret = 0
    for i in range(len(S)+1):
        for j in range(i+1, len(S)+1):
            if int(S[i:j]) % 7 == 0:
                ret += 1
    return ret

def ans(target):
    n = 1
    while n*(n+1)//2 < target: n += 1
    n -= 1
    assert(score("7"*n) <= target <= score("7"*(n+1)))
    a = int("7"*n)
    n += 1
    b = int("7"*n)
    return a, b

print(ans(10**5))