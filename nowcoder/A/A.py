#!/usr/bin/env pypy3

n, m = input().split(' ')
n = int(n)
m = int(m)
A = input().split(' ')
A = list(map(int, A))

for i in range(n):
    print(*A[m*i:m*i+m])
