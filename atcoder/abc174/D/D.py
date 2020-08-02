#!/usr/bin/env pypy3

input()
C = input()

num_red = C.count('R')

ret = 0

for c in C[0:num_red]:
    if c == 'W': ret += 1

print(ret)