#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
VOWELS = "AEIOU"

def cost_c(S, c):
    ret = 0
    for d in S:
        if d == c: continue
        r1 = c in VOWELS
        r2 = d in VOWELS
        if r1 == r2:
            ret += 2
        else:
            ret += 1
    return ret

def ans(S):
    ret = float("inf")
    for c in ALPHABET:
        ret = min(ret, cost_c(S, c))

    return ret

for i in range(read_int()):
    print(f"Case #{i+1}: {ans(input())}")