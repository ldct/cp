#!/usr/bin/env python3

T = int(input())

for t in range(T):
    n, m = input().split(' ')
    n = int(n)
    m = int(m)

    if n % m == 0:
        print("YES")
    else:
        print("NO")