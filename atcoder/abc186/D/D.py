#!/usr/bin/env pypy3

def ans(A):
    A = sorted(A)

    ret = 0
    sum = 0
    for i, a in enumerate(A):
        ret += a*i - sum
        sum += a

    return ret

input()
A = list(map(int, input().split()))
print(ans(A))
