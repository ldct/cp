#!/usr/bin/env python3

from collections import deque

T = int(input())

def ans(maze):
    N = len(maze)
    M = len(maze[0])

    has_g = 'G' in ''.join(''.join(row) for row in maze)

    for x in range(N):
        for y in range(M):
            if maze[x][y] != 'B': continue

            for (dy, dx) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if not (0 <= new_x < N): continue
                if not (0 <= new_y < M): continue

                if maze[new_x][new_y] == "G":
                    return "No"
                elif maze[new_x][new_y] in ["B", "#"]:
                    continue
                elif maze[new_x][new_y] == ".":
                    maze[new_x][new_y] = "#"
                else:
                    assert(False)

    if not has_g:
        return "Yes"

    if maze[N-1][M-1] == '#':
        return "No"
    
    frontier = deque([(N-1, M-1)])

    while len(frontier):
        (x, y) = frontier.popleft()

        for (dy, dx) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if not (0 <= new_x < N): continue
            if not (0 <= new_y < M): continue

            if maze[new_x][new_y] in ["r", "#"]: 
                continue
            elif maze[new_x][new_y] in ["G", "."]:
                maze[new_x][new_y] = "r"
                frontier.append((new_x, new_y))
            else:
                assert(False)

    has_g = 'G' in ''.join(''.join(row) for row in maze)

    if has_g:
        return "No"

    return "Yes"

for t in range(T):
    N, M = input().split(' ')
    N = int(N)
    maze = []
    for _ in range(N):
        row = input()
        maze += [list(row)]

    print(ans(maze))