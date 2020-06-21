#!/usr/bin/env python3

N, K = input().split(' ')
K = int(K)
A = input().split(' ')
A = sorted(list(map(int, A)))

print(sum(A[:K]))