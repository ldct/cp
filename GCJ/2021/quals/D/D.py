#!/usr/bin/env python3

from functools import lru_cache

def fprint(*args):
	print(*args, flush=True)

@lru_cache(None)
def query(a, b, c):
    assert(3 == len(set([a,b,c])))
    fprint(a, b, c)
    return int(input())

[T, N, Q] = list(map(int, input().split()))

for _ in range(T):
    query.cache_clear()
    elems = list(range(1, N+1))

    a = query(1,2,3)
    if a == 1:
        elems[0:3] = [2,1,3]
    elif a == 2:
        pass
    elif a == 3:
        elems[0:3] = [1,3,2]
    else:
        assert(False)

    for k in range(3, N):
        # print("sorting", k, "into place")
        j = k
        while True:
            # print("querying from", elems, j)
            if j == 1:
                a = query(elems[0], elems[1], elems[2])
                if a == elems[0]:
                    elems[0], elems[1] = elems[1], elems[0]
                elif a == elems[1]:
                    j -= 1
                elif a == elems[2]:
                    assert(False)

                j -= 1

            if j-2 < 0: break
            a = query(elems[j-2], elems[j-1], elems[j])
            if a == elems[j-1]:
                break
            elif a == elems[j]:
                elems[j-2], elems[j-1], elems[j] = elems[j-2], elems[j], elems[j-1]
                break
            elif a == elems[j-2]:
                elems[j-2], elems[j-1], elems[j] = elems[j], elems[j-2], elems[j-1]
                j -= 2
            else:
                assert(False)
    fprint(' '.join(map(str, elems)))
    res = input()
    if not (res in '01'):
        print("res=", res)
