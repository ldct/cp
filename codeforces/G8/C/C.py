#!/usr/bin/env pypy3

grid = []
for _ in range(5):
    grid += [[' ']*5000]

def draw(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            grid[i][j] = 'X'
    grid[x+1][y+1] = ' '

N = int(input())

draw(0, 0)
for t in range(1,N+1):
    y = 2*t
    if t % 2 == 1:
        x = 2
    else:
        x = 0
    draw(x, y)

K = 0
for x in range(5):
    for y in range(5000):
        if grid[x][y] == 'X':
            K += 1

print(K)

for x in range(5):
    for y in range(5000):
        if grid[x][y] == 'X':
            print(f"{x} {y}")