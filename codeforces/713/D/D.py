#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

class IndexingList:
    """
    Like a python list, but the `index` is O(1) instead of O(n) time where
    n is the length of the list. In exchange for this speedup, an inverse
    mapping `indexes` is maintained and getting/setting items incurs an
    O(1) overhead to update the inverse mapping.
    """
    from collections import defaultdict
    def __init__(self, lst):
        self.lst = lst
        self.indexes = self.defaultdict(set)
        for i, e in enumerate(self.lst):
            self.indexes[e].add(i)
    def __getitem__(self, k):
        assert(isinstance(k, int))
        return self.lst[k]
    def __setitem__(self, k, v):
        assert(isinstance(k, int))

        old_v = self.lst[k]

        self.indexes[old_v].remove(k)
        self.indexes[v].add(k)
        self.lst[k] = v
    def __len__(self):
        return len(self.lst)
    def index(self, k, exclude=None):
        s = self.indexes[k]
        if len(s) == 0:
            return -1
        for c in s:
            if c != exclude:
                return c
        return -1
    def __repr__(self):
        return self.lst.__repr__()
    def __eq__(self, other):
        if isinstance(other, IndexingList): other = other.lst
        if isinstance(self, IndexingList): self = self.lst
        return self == other

def ans(B):
    B = IndexingList(B)
    S = sum(B)

    for i, b in enumerate(B):
        target = S - b
        if target % 2 == 1: continue
        target = target // 2
        j = B.index(target, exclude=i)
        if j != -1:
            ret = []
            for k, b in enumerate(B):
                if k not in (i, j):
                    ret += [b]
            return ' '.join(map(str, ret))
    return -1

for _ in range(read_int()):
    input()
    B = read_int_list()
    print(ans(B))