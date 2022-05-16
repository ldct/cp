#!/usr/bin/env pypy3

from sys import stdin, stdout, setrecursionlimit

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from functools import lru_cache

def spiralOrder(n):
    m = n
    matrix = []
    for _ in range(n):
        matrix += [['*']*n]

    x, y, dx, dy = 0, 0, 1, 0
    ans = []
    for i in range(1, n*n+1):
        if not 0 <= x+dx < n or not 0 <= y+dy < m or matrix[y+dy][x+dx] != "*":
            dx, dy = -dy, dx

        matrix[y][x] = i
        x, y = x + dx, y + dy

    return matrix

def ans(N, K):
    grid = spiralOrder(N)

    indexOf = dict()
    for i in range(N):
        for j in range(N):
            indexOf[grid[i][j]] = (i, j)

    @lru_cache(None)
    def ans(x, y, K):
        if (x, y) == (0, 0):
            if K == 0:
                return grid[0][0]
            else:
                return 0
        if K == 0:
            return 0

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_x = x + dx
            new_y = y + dy

            if not (0 <= new_x < N): continue
            if not (0 <= new_y < N): continue
            if not (grid[new_x][new_y] < grid[x][y]): continue

            r = ans(new_x, new_y, K-1)
            if r: return grid[new_x][new_y]

        return 0

    c = N // 2

    r = ans(c, c, K)

    if r == 0:
        return None

    ret = [r]

    while r not in [0, 1]:
        i, j = indexOf[r]
        K -= 1
        r = ans(i, j, K)
        ret += [r]

    ret = ret[::-1] + [N*N]

    ret2 = []
    for i in range(len(ret)-1):
        if ret[i] != ret[i+1] - 1:
            ret2 += [(ret[i], ret[i+1])]
    return (len(ret2), ret2)

T = int(input())
for t in range(T):
    r = ans(*read_int_tuple())
    if r is None:
        print("Case #" + str(t+1) + ": IMPOSSIBLE")
    else:
        (y, lines) = r
        print("Case #" + str(t+1) + ": " + str(y))
        for a, b in lines:
            print(a, b)
