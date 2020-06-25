#!/usr/bin/env python3

T = int(input())

def ans(m, C, H):
    d = H - C
    if d % 3 != 0:
        return "Yes"
    if d // 3 > m:
        return "Yes"
    return "No"

for _ in range(T):
    m, C, H = input().split(' ')
    m = int(m)
    C = int(C)
    H = int(H)

    print(ans(m, C, H))