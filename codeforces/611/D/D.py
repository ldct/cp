#!/usr/bin/env python3
import sys, itertools

P = int(10e9) + 7

input()
S = input()

n = len(S)

memo = {}

def numWays(a, minimumStarting):
    # number of ways to split S[a:] where the first thing is at least minimumStarting

    if (a == n):
        return 1
    if (S[a] == "0"):
        return 0

    key = (a, minimumStarting)
    if key in memo:
        return memo[key]

    ans = 0
    for i in range(a+1, n+1):
        firstPart = int(S[a:i], 10)
        if firstPart >= minimumStarting:
            ans = (ans + numWays(i, firstPart+1)) % P

    memo[key] = ans
    return ans

print(numWays(0, 1))
