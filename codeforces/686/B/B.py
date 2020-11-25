#!/usr/bin/env python3

from collections import Counter

def ans(A):
    winning_bid = None
    cA = Counter(A)
    for bid in sorted(set(A)):
        if cA[bid] == 1:
            winning_bid = bid
            break
    if winning_bid is None:
        return -1
    for i in range(len(A)):
        if A[i] == bid:
            return i+1

for _ in range(int(input())):
    input()
    A = list(map(int, input().split()))
    print(ans(A))
