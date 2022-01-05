#!/usr/bin/env pypy3

print(1)
N = 2
print(N)
N *= 2
for _ in range(N):
    row = [1]*N
    print(*row)