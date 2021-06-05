#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(S):

    ret = 0

    num_0 = 0
    num_1 = 0
    parity_0 = None

    def drop(idx):
        nonlocal num_0, num_1, parity_0

        if idx < 0: return
        if S[idx] == '?': return
        if S[idx] == '1': num_1 -= 1
        if S[idx] == '0': num_0 -= 1

        if num_0 + num_1 == 0:
            parity_0 = None


    def ok(idx):
        nonlocal num_0, num_1, parity_0

        if idx >= len(S): return False
        if S[idx] == '?': return True
        if S[idx] == '0':
            if parity_0 is None: return True
            return (parity_0 == (idx%2))
        if S[idx] == '1':
            if parity_0 is None: return True
            return (parity_0 == 1-(idx%2))

    def consume(idx):
        nonlocal num_0, num_1, parity_0

        if S[idx] == '?': return
        if S[idx] == '0':
            num_0 += 1
            parity_0 = idx%2
        if S[idx] == '1':
            num_1 += 1
            parity_0 = 1-idx%2

    j = -1
    for i in range(len(S)):
        # print('before drop', num_0, num_1, parity_0)
        drop(i-1)
        # print('after drop', num_0, num_1, parity_0)

        while ok(j+1):
            j += 1
            consume(j)

        ret += (j-i+1)
        # print(i, j)

    return ret

for _ in range(read_int()):
    print(ans(input()))