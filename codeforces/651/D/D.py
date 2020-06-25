#!/usr/bin/env pypy3

N, K = input().split(' ')
K = int(K)
A = input().split(' ')
A = list(map(int, A))

def choose(start, cost):
    # is it possible to choose n spaces out items starting from `start` all at most cost

    count = 0
    i = start
    last_chosen = None

    while i < len(A):
        if A[i] <= cost:
            last_chosen = i
            count += 1
            i += 2
        else:
            i += 1
    return (count, last_chosen)

from functools import lru_cache

@lru_cache(maxsize=None)
def ok(cost):
    if K % 2 == 0:
        r, lc = choose(0, cost)
        if r >= K//2 and lc != len(A) - 1: return True

        r, lc = choose(1, cost)
        if r >= K//2: return True

    else:
        r, lc = choose(1, cost)
        if r >= K//2 and lc != len(A) - 1: return True # use even

        r, lc = choose(0, cost)
        if r >= (K+1) // 2: return True # use odd

        return False

def ans2():
    for i in range(max(A)):
        if ok(i):
            return i

def ans():
    low = 0
    high = max(A)

    assert(not ok(low))
    assert(ok(high))

    while high - low > 2:
        mid = (low + high) // 2
        if ok(mid):
            high = mid
        else:
            low = mid

    for i in range(low-2, low+100):
        if ok(i):
            return i

print(ans())
