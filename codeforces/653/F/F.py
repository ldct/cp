#!/usr/bin/env pypy3

def swaps(A):
    # assume A is a permutation of range(0, len(A))

    ret = []

    for k in range(len(A)-1, 1, -1):
        assert(A.index(k) <= k)
        # print(f"putting {k} in the correct position")
        while A.index(k) < k:
            s = max(A.index(k)-1, 0)
            ret += [s]
            A[s], A[s+1], A[s+2] = A[s+2], A[s], A[s+1]
            # print(f"A={A}")

    if sorted(A) != A:
        return None

    return [x+1 for x in ret]

def ans(A):

    seen = set()
    duplicate = None
    
    for a in A:
        if a in seen:
            duplicate = a
            break
        else:
            seen.add(a)

    A = [(e, i) for i, e in enumerate(A)]
    A = sorted(A)
    A = [(i, j, e) for j, (e, i) in enumerate(A)]
    A = sorted(A)

    A2 = None

    if duplicate is not None:
        duplicate_indices = set()
        for i, (_, _, e) in enumerate(A):
            if e == duplicate:
                duplicate_indices.add(i)
        assert(len(duplicate_indices) >= 2)
        p, q = list(duplicate_indices)[0:2]
        A2 = A[:]
        A2[p], A2[q] = A2[q], A2[p]
        A2 = [j for (i, j, e) in A2]

    A = [j for (i, j, e) in A]

    # if A2 is None:
    #     print(f"A={A}")
    # else:
    #     print(f"A={A} A2={A2}")

    s = swaps(A)
    s2 = None
    if A2 is not None:
        s2 = swaps(A2)

    if s is not None:
        print(len(s))
        print(*s)
    elif s2 is not None:
        print(len(s2))
        print(*s2)
    else:
        print(-1)

T = int(input())

for _ in range(T):
    input()
    A = input().split(' ')
    A = list(map(int, A))
    ans(A)