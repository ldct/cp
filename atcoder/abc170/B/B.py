#!/usr/bin/env python3

def ans(X, Y):
    TT = Y - 2*X
    if TT < 0:
        return "No"
    if TT % 2 != 0:
        return "No"
    T = TT // 2
    C = X - T
    if C < 0:
        return "No"
    return "Yes"
    
X, Y = input().split(' ')
X = int(X)
Y = int(Y)

print(ans(X, Y))
