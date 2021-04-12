#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(a, b, S):

    S = list(S)
    for i in range(len(S) // 2):
        j = len(S) - i - 1
        if S[i] in '01' and S[j] in '01' and S[i] != S[j]: return -1
        if S[i] == '?' and S[j] in '01': S[i] = S[j]
        if S[j] == '?' and S[i] in '01': S[j] = S[i]

    a -= S.count('0')
    b -= S.count('1')

    if a < 0: return -1
    if b < 0: return -1
    if a + b != S.count('?'): return -1

    for i in range(len(S) // 2):
        j = len(S) - i - 1
        if S[i] == '?' and S[j] == '?':
            if a >= 2:
                S[i] = '0'
                S[j] = '0'
                a -= 2
            elif b >= 2:
                S[i] = '1'
                S[j] = '1'
                b -= 2

    if a + b == 1 and S.count('?') == 1:
        S = ''.join(S).replace('?', '0' if a == 1 else '1')
        return S

    if a + b == 0 and S.count('?') == 0:
        return ''.join(S)

    return -1

for _ in range(read_int()):
    a, b = read_int_tuple()
    S = input()
    print(ans(a, b, S))