#!/usr/bin/env python3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

# print = stdout.write

from collections import defaultdict

def cost(chars):
    freqs = defaultdict(int)
    for c in chars:
        freqs[c] += 1
    return sum(freqs.values()) - max(freqs.values())

def ans(S, N, K):
    to_match = []
    
    for i in range(N // K):
        to_match.append(''.join(S[K*i:K*(i+1)]))

    S = S[::-1]

    for i in range(N // K):
        to_match.append(''.join(S[K*i:K*(i+1)]))

    ret = 0

    for i in range(K):
        chars = [s[i] for s in to_match]
        ret += cost(chars)

    return ret // 2

T = int(input())

for t in range(T):
    N, K = input().split(' ')
    N, K = int(N), int(K)
    S = input().strip()
    print(ans(S, N, K))
