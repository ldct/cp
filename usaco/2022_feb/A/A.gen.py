#!/usr/bin/env pypy3

N = 10
print(N)
for _ in range(N):
    print(*range(1, N+1))

print(1)
print("H"*N)