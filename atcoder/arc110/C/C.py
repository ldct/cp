#!/usr/bin/env python3

def select(s):
	for e in s:
		return e

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
    def index(self, k):
        s = self.indexes[k]
        if len(s) == 0:
            assert(False)
        return next(iter(s))
    def __repr__(self):
        return self.lst.__repr__()
    def __eq__(self, other):
        if isinstance(other, IndexingList):
            return self.lst == other.lst
        elif isinstance(other, list):
            return self.lst == other
        assert(False)

N = int(input())
P = IndexingList(list(map(int, input().split())))

inversions = set()

for i in range(1, N):
	if P.index(i) > P.index(i+1):
		inversions.add(i)

ret = []

while len(inversions):
	x = select(inversions)
	ret += [P.index(x)+1]
	inversions.remove(x)
	P[P.index(x)], P[P.index(x+1)] = P[P.index(x+1)], P[P.index(x)]
	for t in [x-1, x, x+1, x+2]:
		if not (1 <= t <= N-1): continue
		if t in inversions:
			inversions.remove(t)
		if P.index(t) > P.index(t+1):
			inversions.add(t)

	if len(ret) > N:
		break

if sorted(ret) == list(range(1, N)):
	for r in ret:
		print(r)
else:
	print(-1)
