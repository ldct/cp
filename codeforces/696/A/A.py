#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(S):
    ret = []
    last = -1
    for i,c in enumerate(S):
        # print(f"processing {i} {last}")
        valid = []
        for candidate in [0,1]:
            if candidate + int(c) == last:
                continue
            else:
                valid += [candidate]
        ret += [max(valid)]
        last = int(c) + ret[-1]
    return ''.join(map(str,ret))


for _ in range(read_int()):
    input()
    S = input()
    print(ans(S))
