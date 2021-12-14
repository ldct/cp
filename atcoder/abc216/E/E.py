#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from itertools import permutations, chain, combinations
from math import factorial, gcd
from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left

### CODE HERE

# max heap
class MergingHeap:
    def __init__(self, arr):
        freqs = Counter(arr)
        self.elems = []
        for k in freqs:
            self.elems += [(-k, freqs[k])]
        heapify(self.elems)


    def heappop(self):
        assert(len(self.elems))
        ret_e, ret_freq = heappop(self.elems)

        while len(self.elems) and self.elems[0][0] == ret_e:
            ret_freq += self.elems[0][1]
            heappop(self.elems)

        return (ret_e, ret_freq)

    def heappush(self, p):
        if p[1] == 0: return
        heappush(self.elems, p)

def ans(piles, K):
    piles = MergingHeap(piles)
    ret = 0

    while K and len(piles.elems) and piles.elems[0][0] < 0:
        e, f = piles.heappop()

        if f > K:
            ret -= e*K
            return ret

        ret -= e*f
        e += 1
        K -= f

        piles.heappush((e, f))

    return ret


def ans_fast(piles, K):
    piles = MergingHeap(piles)
    ret = 0

    while K and len(piles.elems) and piles.elems[0][0] < 0:
        e, f = piles.heappop()

        e = -e

        if len(piles.elems):
            take_upto = (e + piles.elems[0][0])
        else:
            take_upto = e

        complete_takes = min(take_upto, K // f)

        # for _ in range(complete_takes):
        #     ret += e*f
        #     e -= 1

        ret += f*complete_takes*(e + e - complete_takes + 1) // 2
        e -= complete_takes

        K -= f*complete_takes

        for _ in range(take_upto - complete_takes):
            f_frac = min(f, K)
            ret += e*f_frac
            e -= 1
            K -= f_frac

        piles.heappush((-e, f))

    return ret


if False:
    import random
    for _ in range(100000):
        tc = [random.randint(1, 10**3) for _ in range(100)]
        K = random.randint(1, 10**5)
        assert(ans(tc, K) == ans_fast(tc, K))

else:
    N, K = read_int_tuple()
    piles = read_int_list()
    print(ans_fast(piles, K))
