#!/usr/bin/env python3

A, V = input().split(' ')
A, V = int(A), int(V)
B, W = input().split(' ')
B, W = int(B), int(W)
T = int(input())

if (V - W)*T >= abs(A - B):
    print("YES")
else:
    print("NO")