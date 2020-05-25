#!/usr/bin/env python3
import sys

T = int(input())

def ans(s):
    s = sorted(s)
    N = len(s)

    ans = float("inf")

    for i in range(N-1):
        ans = min(ans, s[i+1] - s[i])

    return ans

for t in range(T):
    input()
    s = input().split(' ')
    s = list(int(x) for x in s)

    print(ans(s))