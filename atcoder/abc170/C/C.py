#!/usr/bin/env python3

def ans(P, X):
    P = set(P)
    for i in range(200):
        if X - i not in P:
            return X-i 
        if X + i not in P:
            return X+i

X, N = input().split(' ')
X = int(X)
N = int(N)
if N == 0:
    print(X)
else:
    P = input().split(' ')
    P = [int(x) for x in P]

    print(ans(P, X))