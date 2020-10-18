#!/usr/bin/env pypy3

def ans(N, grid):
    grid = [list(row) for row in grid]
    a = grid[0][1]
    b = grid[1][0]
    c = grid[N-2][N-1]
    d = grid[N-1][N-2]

    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    def flipa():
        grid[0][1] = 1-a
        print(1, 2)

    def flipb():
        grid[1][0] = 1-b
        print(2, 1)

    def flipc():
        grid[N-2][N-1] = 1-c
        print(N-1, N)

    def flipd():
        grid[N-1][N-2] = 1-d
        print(N, N-1)

    def check():
        a = grid[0][1]
        b = grid[1][0]
        c = grid[N-2][N-1]
        d = grid[N-1][N-2]

        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        assert(a == b)
        assert(c == d)
        assert(b != c)


    if a == b and c == d:
        if b == c:
            print(2)
            flipa()
            flipb()
            check()
            return
        else:
            print(0)
            check()
            return

    if a == b:
        if c == a:
            print(1)
            flipc()
            check()
            return
        elif d == a:
            print(1)
            flipd()
            check()
            return
        else:
            assert(False)

    if c == d:
        if a == c:
            print(1)
            flipa()
            check()
            return
        elif b == c:
            print(1)
            flipb()
            check()
            return

    if a == d:
        assert(b == c)
        print(2)
        flipa()
        flipc()
        check()
        return

    if a == c:
        assert(b == d)
        print(2)
        flipa()
        flipd()
        check()
        return

    assert(False)

def random_grid():
    import random
    return [
        ['S', random.choice("01"), random.choice("01")],
        [random.choice("01"), random.choice("01"), random.choice("01")],
        [random.choice("01"), random.choice("01"), 'F'],
    ]

# for _ in range(1000000):
#     ans(3, random_grid())

for _ in range(int(input())):
    N = int(input())

    grid = []
    for _ in range(N):
        row = input()
        grid += [row]

    ans(N, grid)
