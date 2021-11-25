#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations

### CODE HERE

def ans(S):
    for seed in permutations("abc"):
        full = ''.join(seed)
        full *= (len(S) // 3) + 10
        full = full[0:len(S)]
        if sorted(full) == sorted(S):
            return "YES"
    return "NO"

print(ans(input()))