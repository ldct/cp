#!/usr/bin/env pypy3

def num_dividing(A):
    assert(min(A) > 0)
    # for each d <= max(A), return | { a \in A : d | a }
    # [len([a for a in A if d > 0 and a % d == 0]) for d in range(max(A) +  1)]

    MAX_A = max(A) + 1
    ret = [0]*MAX_A
    cnt = [0]*MAX_A
    for a in A:
        cnt[a] += 1

    for i in range(2, MAX_A):
        for j in range(i, MAX_A, i):
            ret[i] += cnt[j]

    ret[1] = len(A)

    return ret

def num_dividing_slow(A):
    return [len([a for a in A if d > 0 and a % d == 0]) for d in range(max(A) +  1)]

if __name__ == '__main__':
    import random
    for N in range(1, 100):
        for _ in range(100):
            tc = [random.randint(1, 100) for _ in range(N)]
            if not (num_dividing(tc) == num_dividing_slow(tc)):
                print(tc)
