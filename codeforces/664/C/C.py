#!/usr/bin/env pypy3

input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

candidates = []
for a in A:
    candidates += [set(a&b for b in B)]

def has(cs, i):
    for c in cs:
        if c&(1<<i) == 0:
            return True
    return False

def could_az(candidates, i):
    return all(has(cs, i) for cs in candidates)

def weeded(cs, i):
    ret = set(cs)
    for c in cs:
        if c&(1<<i) != 0:
            ret.remove(c)
    assert(len(ret) > 0)
    return ret

ret = [1]*11
for pos in range(10, -1, -1):
    if could_az(candidates, pos):
        ret[pos] = 0
        for i in range(len(candidates)):
            candidates[i] = weeded(candidates[i], pos)

ret = map(str, ret[::-1])
ret = ''.join(ret)
ret = int(ret, 2)
print(ret)