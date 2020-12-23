#!/usr/bin/env pypy3

[H, W] = list(map(int, input().split()))

elems = []

for _ in range(H):
    elems += list(map(int, input().split()))

fl = min(elems)

print(sum([e - fl for e in elems]))
