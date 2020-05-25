#!/usr/bin/env python3
import math

T = int(input())

def ans(n, arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] != '1': continue
            if i == n-1 or j == n-1: continue
            if not (arr[i+1][j] == '1' or arr[i][j+1] == '1'): return "NO"
    return "YES"

for t in range(T):
    n = int(input())
    arr = []
    for i in range(n):
        arr += [input()]
    print(ans(n, arr))