#!/usr/bin/env pypy3

T = int(input())

def ok(r,g,b,w):
    if min(r,g,b,w) < 0: return False

    odds = [x for x in [r,g,b,w] if x % 2 == 1]

    return len(odds) <= 1

def ans(r,g,b,w):
    for _ in range(200):
        if ok(r,g,b,w): return True
        r -= 1
        g -= 1
        b -= 1
        w += 1
    return False

for t in range(T):
    r, g, b, w = input().split()
    r = int(r)
    g = int(g)
    b = int(b)
    w = int(w)

    if ans(r,g,b,w):
        print("Yes")
    else:
        print("No")
