#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import Counter
import sys

### CODE HERE

def sum_triples(arr):
    def sigma(k):
        return sum([a ** k for a in arr])

    return (sigma(1)**3 - 3*sigma(1)*sigma(2) + 2*sigma(3)) // 6

def freq_right(problems):
    # number of right triangles

    freqs0 = Counter([p[0] for p in problems])
    freqs1 = Counter([p[1] for p in problems])

    ret = 0
    for x, y in problems:
        num_l1 = freqs0[x] - 1
        num_l2 = freqs1[y] - 1
        ret += (num_l1 * num_l2)

    return ret

def freq_par_side(problems, idx):
    xs = set([p[idx] for p in problems])
    freqs_idx = Counter([p[idx] for p in problems])
    total = len(problems)

    ret = 0
    for num_line in freqs_idx.values():
        num_rest = total - num_line
        ret += (num_line*(num_line-1)//2) * num_rest

    return ret

def freq_line(problems, _idx):

    freqs = Counter([p[_idx] for p in problems])

    ret = 0
    for v in freqs.values():
        ret += (v*(v-1)*(v-2)) // 6
    return ret


    ret = 0
    for i in range(len(problems)):
        for j in range(i+1, len(problems)):
            for k in range(j+1, len(problems)):
                xs = set()
                ys = set()
                for idx in [i,j,k]:
                    xs.add(problems[idx][0])
                    ys.add(problems[idx][1])
                if len([xs, ys][_idx]) == 1:
                    ret += 1
    return ret

def freq_par(problems):
    # number of triangles where at least one side is parallel
    return freq_par_side(problems, 0) + freq_par_side(problems, 1) + freq_line(problems, 0) + freq_line(problems, 1) - freq_right(problems)

def freqsd(problems):
    # number of triples where every coordinate is different
    N = len(problems)
    return N*(N-1)*(N-2) // 6 - freq_par(problems)

def ans(problems):
    freqs0 = Counter([p[0] for p in problems])
    freqs1 = Counter([p[1] for p in problems])

    a = sum_triples(list(freqs0.values()))
    b = sum_triples(list(freqs1.values()))
    c = freqsd(problems)

    # print(a, b, c)

    return a + b - c

for _ in range(read_int()):
    N = read_int()
    problems = []
    for _ in range(N):
        problems += [read_int_tuple()]
    print(ans(problems))