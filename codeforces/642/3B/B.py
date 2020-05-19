#!/usr/bin/env python3

T = int(input())

def ans(a, b, k):
    a = sorted(a)
    b = sorted(b)[::-1]

    for i in range(min(len(b), k)):
        a[i] = max(a[i], b[i])
    
    return sum(a)

for t in range(T):
    n, k = input().split(' ')
    n = int(n)
    k = int(k)
    a = list(int(x) for x in input().split(' '))
    b = list(int(x) for x in input().split(' '))
    print(ans(a, b, k))