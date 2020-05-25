#!/usr/bin/env python3
import sys

T = int(input())

def ans(a):
    n = len(a)
    num_odds = len(list(x for x in a if x % 2 == 1))

    if num_odds % 2 == 0:
        return "YES"

    s = sorted(a)

    for i in range(n-1):
        if s[i+1] - s[i] == 1:
            return "YES"
    
    return "NO"


for t in range(T):
    input()
    a = input().split(' ')
    a = list(int(x) for x in a)

    print(ans(a))