#!/usr/bin/env pypy3

def ans(L):
    kills = []

    for i, e in enumerate(L):
        start = max(0, i - e)
        end = i
        kills += [(start, -1)]
        kills += [(i, 1)]
    
    kills = sorted(kills)

    # print("kills=", kills)

    prev_i = None
    kill_count = 0
    ret = 0

    for i, d in kills:
        if i != prev_i and prev_i is not None:
            # print(f"checking if {i-1} is alive")
            if kill_count >= 0:
                ret += 1
                # print("yes")
            # print("no")
        kill_count += d
        prev_i = i

    return ret+1


input()
L = input().split(' ')
L = list(map(int, L))

print(ans(L))
