#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

# todo: use range class

B, C = read_int_tuple()

ranges = []

r1 = (B - C//2, B)
ranges += [r1]

C -= 1
if C >= 0:
    r2 = (-B, -B + C//2)
    r3 = (-B - C//2, -B)

    ranges += [r2, r3]

    C -= 1

    if C >= 0:
        r4 = (B, B + C//2)

        ranges += [r4]

# ret = set()
# for a, b in ranges:
#     for i in range(a, b+1):
#         ret.add(i)

def nir(ranges):
    ret = []

    def intersects(i, j, k, l):
        if j < k: return False
        if i > l: return False
        return True

    for (a, b) in ranges:
        intersected = False
        for i, (x, y) in enumerate(ret):
            if intersects(a, b, x, y):
                ret[i] = (min(a, b, x, y), max(a, b, x, y))
                intersected = True
                break
        if not intersected:
            ret += [(a, b)]

    return ret

for _ in range(50):
    ranges = nir(ranges)

ret = 0
for a, b in ranges:
    ret += (b - a + 1)
print(ret)