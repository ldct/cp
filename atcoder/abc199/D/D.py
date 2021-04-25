#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

### CODE HERE

def ans_fast(N, M, edges):

    neighbours = {}
    for i in range(N):
        neighbours[i] = []

    for a, b in edges:
        neighbours[a] += [b]
        neighbours[b] += [a]


    def num_ways(t, i, colouring):

        valid = set("RGB")

        u = t[i]

        for v in neighbours[u]:
            if v in colouring and colouring[v] in valid:
                valid.remove(colouring[v])

        if i+1 >= len(t): return len(valid)

        ret = 0

        for c in valid:
            new_colouring = dict(colouring)
            new_colouring[u] = c

            ret += num_ways(t, i+1, new_colouring)

        return ret

    visited = set()

    def traverse(u, visited):
        visited.append(u)
        for v in neighbours[u]:
            if v in visited: continue
            traverse(v, visited)
        return visited

    ret = 1

    for u in range(N):
        if u in visited: continue
        t = traverse(u, [])
        ret *= num_ways(t, 0, dict())
        for v in t: visited.add(v)

    return ret



def ans_slow(N, M, edges):
    from itertools import product

    def ok(colouring):
        for a, b in edges:
            if colouring[a] == colouring[b]:
                return False
        return True

    ret = 0
    for colouring in product("RGB", repeat=N):
        if ok(colouring):
            ret += 1

    return ret

if False:
    for _ in range(10000):
        import random
        N = 10
        edges = []
        for _ in range(random.randint(0, N*N)):
            a = random.randint(0, N-2)
            b = random.randint(a+1, N-1)
            edges += [(a, b)]

        edges = list(set(edges))

        M = len(edges)

        if ans_fast(N, M, edges) != ans_slow(N, M, edges):
            print(N, M, edges)

else:
    N, M = read_int_tuple()
    edges = []
    for _ in range(M):
        a, b = read_int_tuple()
        a -= 1
        b -= 1
        edges += [(a, b)]

    print(ans_fast(N, M, edges))

# print(ans_slow(N, M, edges))