#!/usr/bin/env python3

def ans(n, k):
    if "0" in str(n):
        return n
    if k == 1:
        return n
    digits = list(int(x) for x in str(n))
    return ans(n + min(digits) * max(digits), k-1)

T = int(input())
for t in range(T):
    n, k = input().split(' ')
    n, k = int(n), int(k)
    print(ans(n, k))