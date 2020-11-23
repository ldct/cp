#!/usr/bin/env python3

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

H, W = input().split()
H = int(H)
W = int(W)

grid = []
for _ in range(H):
    grid += [input()]

def ans(grid, H, W):

    for x in range(H):
        for y in range(W):
            if grid[x][y] == 'S':
                frontier = [(x, y)]

    visited = set(frontier)

    visited_alphabet = set()

    loc_of_alpha = dict()
    for c in ALPHABET:
        loc_of_alpha[c] = set()

    for x in range(H):
        for y in range(W):
            if grid[x][y] in ALPHABET:
                loc_of_alpha[grid[x][y]].add((x, y))

    ret = 1

    while True:
        next_frontier = set()
        for x, y in frontier:
            for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_x = x+dx
                new_y = y+dy

                if not (0 <= new_x < H): continue
                if not (0 <= new_y < W): continue
                if (new_x, new_y) in visited: continue

                if grid[new_x][new_y] == '#': continue
                if grid[new_x][new_y] == 'G': return ret

                assert((grid[new_x][new_y] == '.') or (grid[new_x][new_y] in ALPHABET))

                visited.add((new_x, new_y))
                next_frontier.add((new_x, new_y))

            if (grid[x][y] in ALPHABET) and not (grid[x][y] in visited_alphabet):
                visited_alphabet.add(grid[x][y])

                for point in loc_of_alpha[grid[x][y]]:
                    if point in visited: continue
                    visited.add(point)
                    next_frontier.add(point)

        frontier = next_frontier
        ret += 1

        if len(frontier) == 0: return -1

    return -1

print(ans(grid, H, W))
