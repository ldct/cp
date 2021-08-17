#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

class BCCounter:
    def __init__(self, N=3*10**5+10):
        self.N = N
        self.freqs = [0]*N
        self.freqfreqs = [0]*N

        self.freqfreqs[0] = N

    def inc(self, idx):
        f = self.freqs[idx]
        self.freqfreqs[f] -= 1
        self.freqs[idx] += 1
        self.freqfreqs[f+1] += 1

    def decr(self, idx):
        f = self.freqs[idx]
        self.freqfreqs[f] -= 1
        self.freqs[idx] -= 1
        self.freqfreqs[f-1] += 1

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

### CODE HERE

N, K = read_int_tuple()
candies = read_int_list()

colours = sorted(set(candies))
comp = dict()
for i in range(len(colours)):
    comp[colours[i]] = i

candies = [comp[x] for x in candies]

bcc = BCCounter()

for c in candies[0:K]:
    bcc.inc(c)

ret = 0
ret = max(ret, bcc.num_nonzero())

for i in range(K, len(candies)):
    bcc.inc(candies[i])
    bcc.decr(candies[i-K])
    ret = max(ret, bcc.num_nonzero())

print(ret)