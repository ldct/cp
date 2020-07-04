#!/usr/bin/env pypy3

def all_negative(A):
    for row in A:
        for e in row:
            if e > 0: return False
    return True

n, m = input().split(' ')

n = int(n)
m = int(m)

A = []

for _ in range(n):
    row = input().split(' ')
    row = list(map(int, row))
    A += [row]


# inject test

# n = 90
# m = 90

# A = []
# import random
# for _ in range(n):
#     row = [random.randint(-100, 100) for _ in range(m)]
#     A += [row]

# end inject test



if all_negative(A):
    print(sum(sum(row) for row in A))
    exit(0)

def prefix_sum(row):
    ret = [0]
    for r in row:
        ret += [ret[-1]+r]
    return ret

A_p = list(map(prefix_sum, A))

import array
memo = array.array('i', [2**31-1]*n*m)

def min_from(x, y):
    # minimum if arriving at (x,y) from an upward movement
    if x == 0 and y == 0: return A[x][y]
    if x == -1: return 0

    key = x*m+y
    if memo[key] != 2**31-1: return memo[key]

    if y == 0:
        return A[x][y] + min_from(x-1, y)

    best = float("inf")
    for y_left in range(y+1):
        for y_up in range(y_left,y+1):
            candidate = (A_p[x][y+1] - A_p[x][y_left]) + min_from(x-1, y_up)

            best = min(best, candidate)

    memo[key] = best

    return best


print(min(min_from(n-1,y) for y in range(m)))