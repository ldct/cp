#!/usr/bin/env python3

def ans(A):
    for i in range(len(A)):
        if i+2 >= len(A): break
        [a, b, c] = A[i:i+3]
        if a + b > c: return "YES"
    return "NO"

input() 

A = input().split(' ')
A = list(map(int, A))
A = sorted(A)

print(ans(A))