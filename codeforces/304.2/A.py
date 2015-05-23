#!/usr/bin/env python3

K, N, W = input().split(' ')
K = int(K)
N = int(N)
W = int(W)
cost = int(K * W * (W + 1) / 2)

if cost > N:
    print(cost - N)
else:
    print(0)