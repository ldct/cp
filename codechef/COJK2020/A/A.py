#!/usr/bin/env pypy3

def ok(a, b, c):
    return b + c > a

def ans(A):
    for i in range(len(A)-2):
        [a, b, c] = A[i:i+3]
        if ok(a, b, c):
            print("YES")
            print(a, b, c)
            return
    print("NO")

input()
A = input().split(' ')
A = [int(a) for a in A if len(a)]
A = sorted(A)[::-1]
ans(A)
