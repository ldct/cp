#!/usr/bin/env pypy3

def rod(K, L, R, T, X, Y):
    i = 0
    water = K
    while True:
        if not (L <= water <= R): return i
        if water > K: return float("inf")
        if water + Y <= R: water += Y
        water -= X
        i += 1

[K, L, R, T, X, Y] = list(map(int, input().split()))

print(rod(K, L, R, T, X, Y))