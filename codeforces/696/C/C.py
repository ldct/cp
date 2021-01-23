#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

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
            return False
        for c in s:
            if c != exclude:
                return c
        return False
    def __repr__(self):
        return self.lst.__repr__()
    def __eq__(self, other):
        if isinstance(other, IndexingList):
            return self.lst == other.lst
        elif isinstance(other, list):
            return self.lst == other
        assert(False)

### CODE HERE

def ok(A, target):
    A = IndexingList(A[:])

    n = len(A) // 2
    i = 0

    ret = []

    for _ in range(n):
        while i < len(A) and A[i] == -1:
            i += 1
        if i == len(A): return False
        j = A.index(target - A[i], i)
        if j == False: return False

        target = A[i]

        ret += [(A[i], A[j])]

        A[i] = -1
        A[j] = -1

    return ret

def ans(A):
    A = sorted(A)[::-1]
    for j in range(1, len(A)):
        o = ok(A, A[0] + A[j])
        if o == False:
            continue
        else:
            print("YES")
            print(A[0] + A[j])
            for p in o:
                print(*p)
            return
    print("NO")

for _ in range(read_int()):
    input()
    A = read_int_list()
    ans(A)