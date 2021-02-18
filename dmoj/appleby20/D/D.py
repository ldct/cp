#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(N, edges):
    edges = sorted([tuple(sorted(e)) for e in edges])
    se = set(edges)

    for a, b in edges:
        for c in range(b+1, N+1):
            if (a, c) not in se: continue
            if (b, c) not in se: continue
            return [a, b, c]

    best = None

    for i in range(len(edges)):
        for j in range(i+1, len(edges)):
            e = tuple(sorted(edges[i] + edges[j]))
            if len(set(e)) == 4:
                if best is None:
                    best = e
                else:
                    best = min(best, e)

    if best is None: return -1
    return best

if False:
    import random
    N = 3000
    def r():
        return random.randint(1, N+1)
    edges = [(r(), r()) for _ in range(3000)]
    print(ans(N, edges))

else:
    N, M = read_int_tuple()
    edges = []
    for _ in range(M):
        edges += [read_int_tuple()]

    r = ans(N, edges)
    if r == -1:
        print(-1)
    else:
        print(len(r))
        print(*r)
