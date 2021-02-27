#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

friends = []
for _ in range(read_int()):
    p, w, d, = read_int_tuple()
    friends += [((p - d, p + d), w)]

def ans(friends):
    xs = []
    for (l, r), _ in friends:
        xs += [l,r]

    xs = sorted(set(xs))

    def cost(c):
        ret = 0
        for (l, r), w in friends:
            if l <= c <= r: continue
            ret += w*min(
                abs(l - c), abs(r - c)
            )
        return ret

    if len(xs) == 1: return cost(xs[0])

    lo = xs[0]
    hi = xs[-1]
    while (hi - lo > 1):
        mid = (hi + lo) // 2
        if (cost(mid) < cost(mid + 1)):
            hi = mid
        else:
            lo = mid

    return cost(lo+1)

    return min(cost(i) for i in xs)


print(ans(friends))