#!/usr/bin/env pypy3

T = int(input())

def ans(A):
    odds = []
    evens = []

    for i, a in enumerate(A):
        if a % 2 == 0:
            evens += [i+1]
        else:
            odds += [i+1]
    
    if len(odds) == 0:
        assert(len(evens) >= 2)
        evens = evens[2:]
    elif len(odds) % 2 == 1:
        assert(len(evens) >= 1)
        assert(len(evens) % 2 == 1)
        odds = odds[1:]
        evens = evens[1:]
    else:
        assert(len(odds) >= 2)
        odds = odds[2:]

    assert(len(evens) % 2 == 0)
    assert(len(odds) % 2 == 0)

    for i in range(len(evens) // 2):
        print(f"{evens[2*i]} {evens[2*i+1]}")

    for i in range(len(odds) // 2):
        print(f"{odds[2*i]} {odds[2*i+1]}")

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    ans(A)