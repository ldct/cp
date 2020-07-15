#!/usr/bin/env pypy3

def ans(X, S):
    ret = S.count(X)
    S = set(S)
    for i in range(0, X):
        if i not in S:
            ret += 1
    return ret

N, X = input().split(' ')
N = int(N)
X = int(X)
S = input().split(' ')
S = list(map(int, S))

print(ans(X, S))
