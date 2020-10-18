#!/usr/bin/env pypy3

def ans2(x, y, cx, cy, cxy):
    ret = 0

    xy = min(x, y)

    x -= xy
    y -= xy
    ret += cxy * xy

    ret += x*cx
    ret += y*cy

    return ret

def rotate(x, y):
    return (y, y-x)

def ans(x, y, costs):
    for _ in range(100):
        costs[0] = min(costs[0], costs[1] + costs[5])
        costs[1] = min(costs[1], costs[2] + costs[0])
        costs[2] = min(costs[2], costs[3] + costs[1])
        costs[3] = min(costs[3], costs[4] + costs[2])
        costs[4] = min(costs[4], costs[5] + costs[3])
        costs[5] = min(costs[5], costs[0] + costs[4])

    while not (x >= 0 and y >= 0):
        x, y = rotate(x, y)
        costs = costs[1:] + [costs[0]]

    return ans2(x, y, costs[5], costs[1], costs[0])






for _ in range(int(input())):
    x, y = input().split()
    x = int(x)
    y = int(y)
    costs = input().split()
    costs = list(map(int, costs))
    print(ans(x, y, costs))