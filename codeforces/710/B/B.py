#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(S, K):
    S = list(S)

    def next(i):
        for j in range(i+1, len(S)):
            if S[j] in 'x*': return j
        return -1

    for i in range(len(S)-1, -1, -1):
        if S[i] == '*':
            S[i] = 'x'
            break

    last = None
    for i in range(len(S)):
        if S[i] != '*': continue
        if last is None:
            S[i] = 'x'
            last = i
            continue
        if i - last >= K:
            S[i] = 'x'
            last = i
            continue
        if next(i) - last > K:
            S[i] = 'x'
            last = i
            continue



    return ''.join(S).count('x')

    return S, K

if False:
    # S = '*.***'
    # K = 3
    # print(ans(S, K))
    # print(ans(S[::-1], K))
    # import sys
    # sys.exit(0)

    import random
    for _ in range(10000):
        K = random.randint(1, 5)
        S = ''.join(random.choice('.*') for _ in range(5))
        if not (ans(S, K) == ans(S[::-1], K)):
            print(S, K)
            assert(False)

for _ in range(read_int()):
    N, K = read_int_tuple()
    S = input()
    print(ans(S, K))