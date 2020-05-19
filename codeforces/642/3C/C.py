#!/usr/bin/env python3

T = int(input())

def ans(n):
    n = n // 2
    return 8*(n*(n+1)*(2*n+1))//6


for t in range(T):
    n = int(input())
    print(ans(n))