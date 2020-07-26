#!/usr/bin/env python3

def rating(X):
    if X <= 599: return 8
    if X <= 799: return 7
    if X <= 999: return 6
    if X <= 1199: return 5
    if X <= 1399: return 4
    if X <= 1599: return 3
    if X <= 1799: return 2
    if X <= 1999: return 1

    assert(False)


X = int(input())
print(rating(X))