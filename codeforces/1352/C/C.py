#!/usr/bin/env python3

T = int(input())

for t in range(T):
    n, k = input().split(' ')
    n, k = int(n), int(k)
    print(k + (k-1) // (n-1))