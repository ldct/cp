#!/usr/bin/env python3

def good(N, M, A):
    for x in range(N):
        for y in range(M):
            num_neighbours = 0
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < N and 0 <= new_y < M: num_neighbours += 1
            if num_neighbours < A[x][y]: return False
            A[x][y] = num_neighbours

    return True

def ans(N, M, A):

    if not good(N, M, A):
        print("NO")
        return

    print("YES")
    for row in A:
        print(' '.join(str(e) for e in row))

T = int(input())

for _ in range(T):
    N, M = input().split(' ')
    N = int(N)
    M = int(M)

    A = []

    for _ in range(N):
        row = input().split(' ')
        row = list(map(int, row))
        A += [row]

    ans(N, M, A)