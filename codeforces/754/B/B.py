#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ok(indexes, S):
    subsequence = []
    for i in range(len(S)):
        if i in indexes:
            subsequence += [S[i]]
            S[i] = '?'
    for i in range(len(S)):
        if S[i] == '?':
            S[i] = subsequence.pop()
    return S == sorted(S)

def ans(S):
    S = list(map(int, list(S)))
    if S == sorted(S):
        print(0)
        return
    S = [-1] + S
    sorted_S = sorted(S)

    ret = []
    for i in range(len(sorted_S)):
        if S[i] != sorted_S[i]:
            ret += [i]

    assert(ok(ret, S))

    ret = [len(ret)] + ret

    print(1)
    print(*ret)

if False:
    for _ in range(10000):
        import random
        tc = "".join(random.choice("01") for _ in range(10))
        ans(tc)
else:
    for _ in range(read_int()):
        input()
        ans(input())