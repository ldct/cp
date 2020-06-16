#!/usr/bin/env python3

def ans(A):
    A = sorted(A)
    return A
    
input()
A = input().split(' ')
A = [int(x) for x in A]

print(ans(A))