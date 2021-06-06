#!/usr/bin/env pypy3

from sys import stdin, stdout, exit

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def _int(lst):
    ret = 0
    lst = lst[::-1]
    for i, e in enumerate(lst):
        ret += e*10**i
    return ret

def ok(p, S1, S2, S3):
    S1 = [p[i] for i in S1]
    S2 = [p[i] for i in S2]
    S3 = [p[i] for i in S3]

    if S1[0] == 0: return None
    if S2[0] == 0: return None
    if S3[0] == 0: return None

    S1 = _int(S1)
    S2 = _int(S2)
    S3 = _int(S3)
    if S1 + S2 == S3:
        return S1, S2, S3

    return None

from itertools import permutations

S1 = input()
S2 = input()
S3 = input()

if len(set(S1+S2+S3)) > 10:
    print("UNSOLVABLE")
    exit(0)

alphabet = ''.join(set(S1+S2+S3))

def translate(alphabet, S):
    S = list(S)
    for j in range(len(alphabet)):
        for i in range(len(S)):
            if S[i] == alphabet[j]:
                S[i] = j
    return S

S1 = translate(alphabet, S1)
S2 = translate(alphabet, S2)
S3 = translate(alphabet, S3)

for p in permutations(range(10)):
    r = ok(p, S1, S2, S3)
    if r is not None:
        for line in r: print(line)
        exit(0)

print("UNSOLVABLE")