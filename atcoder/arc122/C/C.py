#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from functools import lru_cache

### CODE HERE

@lru_cache(None)
def f(n):
    if n < 2: return n
    return (f(n-1) + f(n-2))

FIB = [f(i) for i in range(100)]

def zeck(N):
    if N in FIB: return [N]

    for i in range(len(FIB)-1, -1, -1):
        if FIB[i] < N:
            return [FIB[i]] + zeck(N-FIB[i])

def sim(ops):
    state = [0, 0]
    for op in ops:
        [x, y] = state
        if op == 1:
            state = [x+1, y]
        if op == 2:
            state = [x, y+1]
        if op == 3:
            state = [x+y, y]
        if op == 4:
            state = [x, x+y]

    return state

def inserted(arr, idx, elem):
    arr = arr[:]
    arr.insert(idx, elem)
    return arr

def modify(ops, target):
    for i in range(len(ops)-1, -1, -1):
        if sim(inserted(ops, i, 1))[0] == target:
            return inserted(ops, i, 1)
        if sim(inserted(ops, i, 2))[0] == target:
            return inserted(ops, i, 2)

def ans(N):
    if N < 100: return [1]*N

    Z = zeck(N)

    ops = [1,2,3]
    state = [2,1]
    while max(state) != Z[0]:
        ops += [7-ops[-1]]
        if ops[-1] == 3:
            state = [sum(state), state[1]]
        else:
            assert(ops[-1] == 4)
            state = [state[0], sum(state)]

    if state[0] < state[1]:
        state = state[::-1]
        ops = [1, 2] + [7 - s for s in ops[2:]]

    assert(sim(ops) == state)

    Z = Z[1:]
    for z in Z:
        ops = modify(ops, z+sim(ops)[0])

    assert(sim(ops)[0] == N)

    return ops

ops = ans(read_int())

print(len(ops))
for r in ops: print(r)