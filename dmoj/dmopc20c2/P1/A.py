#!/usr/bin/env pypy3

N = int(input())
commands = input()

ret = []
for _ in range(3*N+10):
    ret += [list("."*N)]

x = N
y = 0

for c in commands:
    if c == "^":
        ret[x][y] = "/"
        x -= 1
    elif c == "v":
        x += 1
        ret[x][y] = "\\"
    elif c == ">":
        ret[x][y] = "_"
    else:
        assert(False)
    y += 1


for row in ret:
    r = ''.join(row)
    if r.count(".") == N: continue
    print(r)