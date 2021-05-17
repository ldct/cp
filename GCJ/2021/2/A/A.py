#!/usr/bin/env python3

def fprint(*args):
	print(*args, flush=True)

[T, N] = list(map(int, input().split()))

for _ in range(T):
    for i in range(1, N):
        fprint(f"M {i} {N}")
        j = int(input())
        for t in range(j-i):
            s = j - t
            fprint(f"S {s-1} {s}")
            input()
    fprint("D")
    assert(input() == "1")
