#!/usr/bin/env python3

def ans(S, X):
    for c in S:
        if c == 'o':
            X += 1
        elif (c == 'x') and (X > 0):
            X -= 1
    return X

N, X = input().split()
S = input()

print(ans(S, int(X)))