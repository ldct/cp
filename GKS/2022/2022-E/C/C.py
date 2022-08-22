#!/usr/bin/env python3

from sys import stdin, stdout
import random

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def short(S):
    N = len(S)
    for i in range(1, len(S)+1):
        if not (N % i == 0): continue
        s = S[0:i]
        if not (s == s[::-1]): continue
        if not (S == s*(N // i)): continue
        return s
    return S

def ans(S):
    return short(S)

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

if True:
    N = 2**20
    s = ''.join(random.choice(ALPHABET) for _ in range(N))
    print(len(short(s)))
else:
    T = int(input())
    for t in range(T):
        input()
        S = input()
        print("Case #" + str(t+1) + ": " + str(ans(S)))
