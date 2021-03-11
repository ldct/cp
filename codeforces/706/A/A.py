#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(K, S):
    i = 0
    j = len(S)-1
    for _ in range(K):
        if S[i] != S[j]:
            return 'NO'
        i += 1
        j -= 1
    if i > j: return 'NO'
    return 'YES'

for _ in range(read_int()):
    _, K = read_int_tuple()
    print(ans(K, input()))