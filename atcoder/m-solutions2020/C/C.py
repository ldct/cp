#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

N, K = input().split(' ')
N = int(N)
K = int(K)
A = input().split(' ')
A = list(map(int, A))

for i in range(N-K):
    a = A[i]
    b = A[i+K]

    if b > a:
        print("Yes")
    else:
        print("No")

