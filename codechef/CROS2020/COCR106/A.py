#!/usr/bin/env python3

T = int(input())

def ok(A, num):
    generosity = [num - a for a in A]
    s = 0
    for g in generosity:
        s += g
        if s < 0: return False
    return True

def ans(A):
    low = A[0] - 1
    high = max(A) + 1

    assert(not ok(A, low))
    assert(ok(A, high))

    while high - low > 2:
        mid = (low + high) // 2
        if ok(A, mid):
            high = mid
        else:
            low = mid

    return low+1

    # for i in range(A[0]-1, max(A)+1):
    #     if ok(A, i):
    #         return i

for _ in range(T):
    N = int(input())
    A = input().split(' ')[0:N]
    A = [int(a) for a in A]
    print(ans(A))
