#!/usr/bin/env pypy3

class IndexingList:
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

num_calls = 0

def swaps(A):
    global num_calls

    # assume A is a permutation of range(0, len(A))

    A = IndexingList(A)
    ret = []

    for k in range(len(A)-1, 1, -1):
        assert(A.index(k) <= k)
        # print(f"putting {k} in the correct position")
        while A.index(k) < k:
            num_calls += 1
            s = max(A.index(k)-1, 0)
            ret += [s]
            A[s], A[s+1], A[s+2] = A[s+2], A[s], A[s+1]
            # print(f"A={A}")

    if sorted(A) != A:
        return None

    return [x+1 for x in ret]

# timing code
# swaps(list(range(2000))[::-1])
# exit(0)

def ans(A):

    seen = set()
    duplicate = None
    
    for a in A:
        if a in seen:
            duplicate = a
            break
        else:
            seen.add(a)

    A = [(e, i) for i, e in enumerate(A)]
    A = sorted(A)
    A = [(i, j, e) for j, (e, i) in enumerate(A)]
    A = sorted(A)

    A2 = None

    if duplicate is not None:
        duplicate_indices = set()
        for i, (_, _, e) in enumerate(A):
            if e == duplicate:
                duplicate_indices.add(i)
        assert(len(duplicate_indices) >= 2)
        p, q = list(duplicate_indices)[0:2]
        A2 = A[:]
        A2[p], A2[q] = A2[q], A2[p]
        A2 = [j for (i, j, e) in A2]

    A = [j for (i, j, e) in A]

    # if A2 is None:
    #     print(f"A={A}")
    # else:
    #     print(f"A={A} A2={A2}")

    s = swaps(A)
    s2 = None
    if A2 is not None:
        s2 = swaps(A2)

    if s is not None:
        print(len(s))
        print(*s)
    elif s2 is not None:
        print(len(s2))
        print(*s2)
    else:
        print(-1)

T = int(input())

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    ans(A)