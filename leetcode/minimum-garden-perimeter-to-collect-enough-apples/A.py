#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def apples_in(N):
    return N*(N+1)*(2*N+1)*2

def min_square(needed):
    low = 0
    high = 10**10

    def ok(x):
        return apples_in(x) >= needed

    while high - low > 2:
        assert not ok(low)
        assert ok(high)
        mid = (low + high) // 2
        if ok(mid):
            high = mid
        else:
            low = mid

    for i in range(low, low+5):
        if ok(i): return i

def ans(needed):
    side = 2*min_square(needed)
    return 4*side

# print(apples_in(0))
# print(apples_in(1))

print(ans(1))
print(ans(13))
print(ans(1000000000))