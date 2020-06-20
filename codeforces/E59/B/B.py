#!/usr/bin/env python3

T = int(input())

for _ in range(T):
    k, x = input().split(' ')
    k = int(k)
    x = int(x)
    print(x + (k-1)*9)
