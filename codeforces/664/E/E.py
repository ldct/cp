#!/usr/bin/env pypy3

from collections import Counter

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)

neighbours = dict()

for i in range(1, n+1):
    neighbours[i] = []

for _ in range(m):
    u, v, w = input().split()
    u = int(u)
    v = int(v)
    w = int(w)

    neighbours[u] += [(w, v)]

for i in range(1, n+1):
    neighbours[i] = sorted(neighbours[i])

rules = []

for a in range(1,2):
    for b in range(1,3):
        for c in range(1,4):
            for d in range(1,5):
                for e in range(1,6):
                    for f in range(1,7):
                        for g in range(1,8):
                            for h in range(1,9):
                                for i in range(1,10):
                                    rules += [(a,b,c,d,e,f,g,h,i)]

k_rules = set()

for r in rules:
    k_rules.add(r[:k])

def okv(v):
    for k in v:
        if v[k] != 2: return False
    return True

def ok(rule):
    visited = set()

    p = 1

    for _ in range(n):
        if p in visited:
            return False
        visited.add(p)
        p_outdegree = len(neighbours[p])
        _, p = neighbours[p][rule[p_outdegree-1]-1]

    return p == 1

ret = 0

for rule in k_rules:
    if ok(rule):
        # print(rule)
        ret += 1
        
print(ret)