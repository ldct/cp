#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def all_uniq(lst):
    return len(lst) == len(set(lst))

def ans(A):
    i = None
    known = []
    for a in A:
        # print(known, i)
        assert(all_uniq(known))
        if len(known) == 0:
            known += [a]
            i = 0
            continue
        if known[i] == a:
            continue
        elif known[i] < a:
            if a in known[i:i+2]:
                i = known.index(a)
                continue
            if len(known[i:i+2]) == 2: return False
            known += [a]
            known = sorted(known)
            i = known.index(a)
        else:
            assert(a < known[i])
            i2 = max(i-2, 0)
            if a in known[i2:i]:
                i = known.index(a)
                continue
            if len(known[i2:i]) == 2: return False
            known += [a]
            known = sorted(known)
            i = known.index(a)

    return True

for _ in range(read_int()):
    input()
    print("YES" if ans(read_int_list()) else "NO")
