#!/usr/bin/env pypy3

A, B, K = input().split()
A = int(A)
B = int(B)
K = int(K)

e1 = min(A, K)
A -= e1
K -= e1
B -= min(B, K)
print(A, B)