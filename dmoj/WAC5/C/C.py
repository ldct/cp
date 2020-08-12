#!/usr/bin/env pypy3

from collections import Counter
import array

class BCCounter:
    def __init__(self, N=2*10**5+10):
        self.N = N
        self.freqs = [0]*N
        self.freqfreqs = [0]*N

        # self.freqfreqs[0] = N

    def inc(self, idx):
        f = self.freqs[idx]
        # self.freqfreqs[f] -= 1
        self.freqs[idx] += 1
        # self.freqfreqs[f+1] += 1

    def decr(self, idx):
        f = self.freqs[idx]
        # self.freqfreqs[f] -= 1
        self.freqs[idx] -= 1
        # self.freqfreqs[f-1] += 1

    def nice_freqs(self):
        r = dict()
        for i in range(self.N):
            if self.freqs[i] != 0:
                r[i] = self.freqs[i]
        return r

    def nice_ff(self):
        r = dict()
        for i in range(self.N):
            if self.freqfreqs[i] != 0:
                r[i] = self.freqfreqs[i]
        return r     

    def num_nonzero(self):
        return self.N - self.freqfreqs[0]

    def check(self):
        nn = 0
        for i in range(len(self.freqs)):
            assert(self.freqs[i] == self._counter[i])
            if self._counter[i] != 0:
                nn += 1
        assert(nn == self.num_nonzero())

import math
if True:
    import random
    B = [random.randint(1, 2*10**5-10) for _ in range(2*10**5)]
    ub = math.floor(math.sqrt(len(B)))
else:
    input()
    B = input().split()
    B = list(map(int, B))


ret = 0

ub = math.floor(math.sqrt(len(B)))

if max(B) <= 2:
    ub = 3

def ok(c, side):
    return True
    return c.freqfreqs[side] == side

for side in range(1, ub+1):
    square = side*side
    # print("checking", square)

    c = BCCounter()
    for b in B[:square]:
        c.inc(b)

    if ok(c, side):
        ret += 1

    i = 0
    j = square
    while j < len(B):
        c.decr(B[i])
        c.inc(B[j])

        if ok(c, side):
            ret += 1

        i += 1
        j += 1

print(ret)