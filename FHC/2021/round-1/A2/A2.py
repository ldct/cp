#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

MODULUS = 10**9 + 7

### CODE HERE

def ans_slow(S):
    def F(S):
        S = S.replace('F', '')
        ret = 0
        for i in range(len(S)-1):
            if S[i] != S[i+1]:
                ret += 1
        return ret

    ret = 0
    for i in range(len(S)+1):
        for j in range(i, len(S)+1):
            ret += F(S[i:j])
    return ret

def ans(S):
    non_F = []
    for i, c in enumerate(S):
        if c == 'F': continue
        non_F += [i]

    ret = 0

    for idx in range(len(non_F)-1):
        if S[non_F[idx]] == S[non_F[idx+1]]: continue
        i, j = non_F[idx], non_F[idx+1]

        a = i+1
        b = len(S)-j

        ret += a*b
        ret %= MODULUS

    return ret

for t in range(read_int()):
    input()
    S = input()
    print(f"Case #{t+1}: {ans(S)}")