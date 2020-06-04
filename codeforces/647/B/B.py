#!/usr/bin/env python3

def ans(s):
    s = set(s)
    for i in range(1, 1024+1):
        new_s = set(x ^ i for x in s)
        if new_s == s:
            return i
    return -1

T = int(input())

for t in range(T):
    n = input()
    s = input().split(' ')
    s = list(int(x) for x in s)
    print(ans(s))
