#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2500)

from collections import defaultdict

children = defaultdict(set)
num_bigger = dict()
ans = dict()

n = int(input())

root = None

for me in range(1, n+1):
    parent, b = input().split(' ')
    parent, b = int(parent), int(b)
    num_bigger[me] = b
    if parent == 0:
        root = me
    else:
        children[parent].add(me)

assert(root)

def sorted_of(elem):
    ret = []
    for child in children[elem]:
        ret += sorted_of(child)
    if num_bigger[elem] <= len(ret):
        ret.insert(num_bigger[elem], elem)
    else:
        print("NO")
        sys.exit()
    return ret

s = sorted_of(root)
    
for i in range(n):
    ans[s[i]] = i+1

print("YES")
print(' '.join(str(ans[i]) for i in range(1, n+1)))
