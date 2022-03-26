#!/usr/bin/env pypy3

import io, os, sys
from sys import stdin, stdout

# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def dijkstra(graph, start):
    """ Uses Dijkstra's algortihm to find the shortest path between in a graph. """
    from heapq import heappop, heappush

    dist = defaultdict(lambda: float("inf"))
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len != dist[v]: continue

        for w, edge_len in graph[v]:
            candidate = path_len + edge_len
            if candidate < dist[w]:
                dist[w] = candidate
                heappush(queue, (candidate, w))

    return dist

def get_substrings(S):
    ret = set()
    for i in range(len(S)):
        for j in range(i, len(S)+1):
            ret.add(S[i:j])
    return ret

def ans(S, A, B, C):
    substrings = list(get_substrings(S))

    neighbours = defaultdict(list)

    def add_edge(x, y, cost):
        neighbours[x].append((y, cost))

    for X in substrings:
        for Y in substrings:

            # type a character
            for c in ALPHABET:
                if X + c in substrings:
                    add_edge((X, Y), (X+c, Y), A)

            # cut
            add_edge((X, Y), ("", X), B)

            # paste
            if X + Y in substrings:
                add_edge((X, Y), (X+Y, Y), C)

    distance = dijkstra(neighbours, ("", ""))
    ret = float("inf")
    for (X, Y) in distance:
        if X == S:
            ret = min(ret, distance[(X, Y)])

    return ret

input()
print(ans(input(), read_int(), read_int(), read_int()))