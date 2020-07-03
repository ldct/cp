#!/usr/bin/env pypy3

def all_zero(A):
    for row in A:
        for e in row:
            if e != 0: return False
    return True

n, m = input().split(' ')
n = int(n)
m = int(m)

A = []

for _ in range(n):
    row = input().split(' ')
    row = list(map(int, row))
    A += [row]

moves = []

# produce a zero

min_elem = min(min(row) for row in A)

if min_elem > 0:
    if m >= n:
        for x in range(n):
            moves += [f"row {x+1}"]*min_elem
    else:
        for y in range(m):
            moves += [f"col {y+1}"]*min_elem

    for x in range(n):
        for y in range(m):
            A[x][y] -= min_elem

pivot = None

for x in range(n):
    for y in range(m):
        if A[x][y] == 0:
            pivot = (x, y)
            break

assert(pivot is not None)

pivot_x, pivot_y = pivot

for x in range(n):
    if x == pivot_x: continue
    f = A[x][pivot_y]
    moves += [f"row {x+1}"]*f
    for y in range(m):
        A[x][y] -= f

for y in range(m):
    if y == pivot_y: continue
    f = A[pivot_x][y]
    moves += [f"col {y+1}"]*f
    for x in range(n):
        A[x][y] -= f

if not all_zero(A):
    print(-1)
else:
    print(len(moves))
    print('\n'.join(moves))
