#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

H, W = input().split()
H = int(H)
W = int(W)

Cx, Cy = input().split()
Cx = int(Cx)
Cy = int(Cy)

Dx, Dy = input().split()
Dx = int(Dx)
Dy = int(Dy)

matrix = []

for _ in range(H):
    row = list(input())
    matrix += [row]

# print("reading done")

from collections import deque


visited = set()

def bfs(x, y, label):
    global visited
    worklist = deque([(x, y)])
    while len(worklist):
        (x, y) = worklist.popleft()
        matrix[x][y] = label
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x+dx, y+dy
            if 0 <= new_x < H and 0 <= new_y < W and matrix[new_x][new_y] == '.' and (new_x, new_y) not in visited:
                worklist.append((new_x, new_y))
                visited.add((new_x, new_y))
    
# for row in matrix:
#     print(''.join(map(str, row)))

curr_label = 0
for x in range(0, H):
    for y in range(0, W):
        if matrix[x][y] == '.':
            bfs(x, y, curr_label)
            curr_label += 1

# for row in matrix:
#     print(''.join(map(str, row)))

# print("cc done")

neighbours = []

for _ in range(0, curr_label):
    neighbours += [set()]

for x in range(H):
    for y in range(W):
        u = matrix[x][y]
        if u == '#': continue
        for dx in [-2, -1, 0, 1, 2]:
            for dy in [-2, -1, 0, 1, 2]:
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x < H and 0 <= new_y < W and matrix[new_x][new_y] != '#':
                    v = matrix[new_x][new_y]
                    if u == v: continue

                    neighbours[u].add(v)
                    neighbours[v].add(u)

Cx -= 1
Cy -= 1

Dx -= 1
Dy -= 1

source = matrix[Cx][Cy]
target = matrix[Dx][Dy]

import sys

if source == '#' or target == '#':
    print(-1)
    sys.exit(0)

visited = set([source])
frontier = set([source])

if target in frontier:
    print(0)
    sys.exit(0)

# print(neighbours, source, target)

count = 1
while len(frontier):
    next_frontier = set()
    for u in frontier:
        for v in neighbours[u]:
            if v not in visited:
                visited.add(v)
                next_frontier.add(v)
    if target in next_frontier:
        print(count)
        count += 1
        sys.exit(0)

    count += 1
    frontier = next_frontier

print(-1)
