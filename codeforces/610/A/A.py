#!/usr/bin/env python3
import sys

N = int(input())

def ans(N):
    if N % 2 == 1:
        return 0
    half = N/2

    if half % 2 == 0:
        return int(half / 2 - 1)
    if half % 2 == 1:
        return int((half - 1) / 2)

print(ans(N))