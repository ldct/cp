#!/usr/bin/env python3

S = input()
T = input()

assert(len(S) == len(T))

ans = 0

for i in range(len(S)):
    if S[i] != T[i]: ans += 1

print(ans)