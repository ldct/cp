#!/usr/bin/env python3

input()
A = input().split(' ')
A = list(map(int, A))

ret = 0
for i, a in enumerate(A):
    if i % 2 == 0 and a % 2 == 1:
        ret += 1

print(ret)