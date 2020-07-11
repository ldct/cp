#!/usr/bin/env python3

N, H = input().split(' ')
H = int(H)
T = input().split(' ')
T = list(map(int, T))

print(*[t + H for t in T])