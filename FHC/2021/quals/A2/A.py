#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def enc(c):
    return ord(c) - ord('A')

def ans_c(S, c, cost):
    ret = 0
    for d in S:
        ret += cost[enc(d)][enc(c)]
    return ret

def ans(S, paths):
    cost = []
    for _ in range(26):
        cost += [[float("inf")]*26]
    for i in range(26):
        cost[i][i] = 0
    for a, b in paths:
        i = enc(a)
        j = enc(b)
        cost[i][j] = 1

    for k in range(26):
        for i in range(26):
            for j in range(26):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    ret = float("inf")
    for c in ALPHABET:
        ret = min(ret, ans_c(S, c, cost))

    if ret == float("inf"): return -1
    return ret

for t in range(read_int()):
    S = input()
    paths = [input() for _ in range(read_int())]
    print(f"Case #{t+1}: {ans(S, paths)}")