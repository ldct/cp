#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

### CODE HERE

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

class UnionFind:
    def __init__(self, words):
        self.parent = dict()
        for w in words:
            self.parent[w] = w

    def poke(self, w):
        if w not in self.parent:
            self.parent[w] = w

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def join(self, a, b):
        self.parent[self.find(b)] = self.find(a)

def score(w):
    ret = 0
    for c in w:
        ret |= (1 << (ord(c) - ord('a')))
    return ret

class Solution:
    def groupStrings(self, words):
        l_words = [score(w) for w in words]
        words = set(l_words)

        uf = UnionFind(words)

        for w in words:
            for c in ALPHABET:
                new_w = w & ~score(c)

                uf.poke(new_w)
                uf.join(w, new_w)

        P = defaultdict(int)
        for w in l_words:
            P[uf.find(w)] += 1

        return len(P), max(P.values())



s = Solution()

TC = ["web","a","te","hsx","v","k","a","roh"]
print(s.groupStrings(TC))
