#!/usr/bin/env python3

T = int(input())

def ans(A):
    m = max(A)

    for a in A:
        if (m - a) % 2 != 0: return "NO"
    
    return "YES"
    
for _ in range(T):
    input()
    A = input().split(' ')
    A = [int(x) for x in A]
    print(ans(A))
