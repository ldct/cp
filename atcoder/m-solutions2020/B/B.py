#!/usr/bin/env python3

def count(A, B, C):
    ret = 0
    while B <= A:
        B *= 2
        ret += 1
    while C <= B:
        C *= 2
        ret += 1
    return ret
    
A, B, C = input().split(' ')
K = int(input())

A = int(A)
B = int(B)
C = int(C)

if count(A, B, C) <= K:
    print("Yes")
else:
    print("No")