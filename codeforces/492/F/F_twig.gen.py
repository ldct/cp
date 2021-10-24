#!/usr/bin/env pypy3

N = 3000
D = 10

print(N, D)
for i in range(2, N+1):
    if i in [2, 3]:
        print(1)
    else:
        print(i-2)
