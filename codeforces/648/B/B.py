#!/usr/bin/env python3

T = int(input())

def ans(A, B):
    arr = list(zip(A, B))

    zeroes = [a for (a, b) in arr if b == 0]
    ones = [a for (a, b) in arr if b == 1]

    if len(ones) > 0 and len(zeroes) > 0:
        return "Yes"

    if len(ones) > 0:
        if sorted(ones) == ones:
            return "Yes"
        return "No"

    if len(zeroes) > 0:
        if sorted(zeroes) == zeroes:
            return "Yes"
        return "No" 

    assert(False)

for t in range(T):
    N = int(input())
    A = input().split(' ')
    A = [int(x) for x in A]
    B = input().split(' ')
    B = [int(x) for x in B]

    print(ans(A, B))