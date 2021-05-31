#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

input()
S = read_int_list()

def ans_single(S):
    prefixes = [0]
    for s in S: prefixes += [prefixes[-1] + s]

    def score(i, j):
        return abs(2*(prefixes[j] - prefixes[i]) - prefixes[-1])

    return min(score(0, i) for i in range(len(prefixes)))

def ans_slow(S):
    ret = []
    ret += [ans_single(S)]
    for _ in range(len(S)-1):
        S = S[1:] + [S[0]]
        ret += [ans_single(S)]
    return ret

def ans(S):
    N = len(S)
    target = sum(S)

    def score(s):
        return abs(2*s - target)

    S += S

    run = 0
    i = 0
    ret = []

    for k in range(N):
        while score(run + S[i]) < score(run):
            run += S[i]
            i += 1

        ret += [score(run)]
        # ret += [(i, run, score(run))]

        run -= S[k]


    return ret

print(*ans(S))