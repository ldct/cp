#!/usr/bin/env pypy3

class IndexingList:
    from collections import defaultdict
    def __init__(self, lst):
        self.lst = lst
        self.indexes = self.defaultdict(list)
        for i, e in enumerate(self.lst):
            self.indexes[e] += [i]
    def __getitem__(self, k):
        assert(isinstance(k, int))
        return self.lst[k]
    def __setitem__(self, k, v):
        assert(False)
    def __len__(self):
        return len(self.lst)
    def __repr__(self):
        return self.lst.__repr__()

class BIT:
    def __init__(self, arg):
        if isinstance(arg, int):
            self.sumtree = [0] * arg
        else:
            self.sumtree = list(arg)
            for (i, val) in enumerate(self.sumtree):
                # For each consecutive 1 in the lowest order bits of i
                j = 1
                while i & j != 0:
                    val += self.sumtree[i ^ j]
                    j <<= 1
                self.sumtree[i] = val


    def __len__(self):
        return len(self.sumtree)


    def __getitem__(self, index):
        if not (0 <= index < len(self)):
            raise IndexError()
        result = self.sumtree[index]
        # For each consecutive 1 in the lowest order bits of index
        i = 1
        while index & i != 0:
            result -= self.sumtree[index ^ i]
            i <<= 1
        return result


    def __setitem__(self, index, val):
        if not (0 <= index < len(self)):
            raise IndexError()
        self.add(index, val - self[index])


    def add(self, index, delta):
        if not (0 <= index < len(self)):
            raise IndexError()
        while index < len(self):
            self.sumtree[index] += delta
            index |= index + 1  # Set lowest 0 bit; strictly increasing


    def get_total(self):
        return self.get_prefix_sum(len(self))


    def get_prefix_sum(self, end):
        if not (0 <= end <= len(self)):
            raise IndexError()
        result = 0
        while end > 0:
            result += self.sumtree[end - 1]
            end &= end - 1  # Clear lowest 1 bit; strictly decreasing
        return result


    def get_range_sum(self, start, end):
        if not (0 <= start <= end <= len(self)):
            raise IndexError()
        ret = self.get_prefix_sum(end) - self.get_prefix_sum(start)
        return ret

    def __repr__(self):
        return f"BIT{[self[i] for i in range(len(self))]}"


from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

N, K, Q = read_int_tuple()
A = IndexingList(read_int_list())

arr = BIT(N)

inversions = []
counts = []

for k in range(1, K+1):
    A.indexes[k] = sorted(A.indexes[k])
    ti = 0
    for i in A.indexes[k]:
        ti += arr.get_range_sum(i, len(arr))
        arr[i] += 1
    inversions += [ti]
    counts += [len(A.indexes[k])]

counts = BIT(counts)

print(inversions)
print(counts)

for _ in range(Q):
    q = read_int()
    a, b = q-1, q