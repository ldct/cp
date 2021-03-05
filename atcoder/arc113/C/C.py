#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans_slow(S):
    S = list(S)
    for i in range(len(S)-2, -1, -1):
        if S[i] == S[i+1] and len(set(S[i:])) > 1:
            ret = 0
            for j in range(i+2, len(S)):
                if S[j] != S[i]:
                    ret += 1
                S[j] = S[i]
            return ret + ans_slow(''.join(S))
    return 0

def ans(S):
    ret = 0
    S = list(S)
    j = len(S)-1
    while j >= 0 and S[j] == S[-1]:
        j -= 1
    i = j
    j += 1
    if j == 0: return 0
    while i > 0:
        if S[i-1] == S[i]:
            for k in range(i+1, j):
                if S[k] != S[i]:
                    ret += 1
                S[k] = S[i]
            if S[-1] != S[i]:
                ret += len(S)-j
            S[-1] = S[i]
            j = i
        i -= 1
    return ret

# import random
# for _ in range(100000):
#     tc = ''.join(random.choice("abcd") for _ in range(20))
#     assert(ans(tc) == ans_slow(tc))
# import sys
# sys.exit(0)

S = input()
print(ans(S))