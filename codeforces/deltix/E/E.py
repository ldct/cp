#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from itertools import product

N = 13
NO_ABC = []
NO_AB = []
NO_BC = []
for _ in range(N):
    NO_AB += [[]]
    NO_BC += [[]]
    NO_ABC += [[]]

def no_abc(S):
    for i in range(len(S)):
        if S[i] != 'a': continue
        for j in range(i+1, len(S)):
            if S[j] != 'b': continue
            for k in range(j+1, len(S)):
                if S[k] != 'c': continue
                return False
    return True

def no_ab(S):
    for i in range(len(S)):
        if S[i] != 'a': continue
        for j in range(i+1, len(S)):
            if S[j] != 'b': continue
            return False
    return True

def no_bc(S):
    for i in range(len(S)):
        if S[i] != 'b': continue
        for j in range(i+1, len(S)):
            if S[j] != 'c': continue
            return False
    return True

for n in range(N):
    for S in product('abc', repeat=n):
        s = ''.join(S)
        if no_abc(s): NO_ABC[n] += [s]
        if no_ab(s): NO_AB[n] += [s]
        if no_bc(s): NO_BC[n] += [s]

def mismatches(A, B):
    ret = 0
    assert(len(A) == len(B))
    for i in range(len(A)):
        if A[i] != B[i]: ret += 1
    return ret

def ans_slow(S):
    return min(mismatches(S, G) for G in NO_ABC[len(S)])

def ans_slow_ab(S):
    return min(mismatches(S, G) for G in NO_AB[len(S)])

def ans_slow_bc(S):
    return min(mismatches(S, G) for G in NO_BC[len(S)])

def has_subseq(S, x, y):
    for i in range(len(S)):
        for j in range(i, len(S)):
            if S[i] == x and S[j] == y: return True
    return False


# ab a
def ans_dc(S):
    def ans(i, j):
        # a, b, c, ab, bc
        if i == j:
            if S[i] == 'a': return (1, 0, 0, 0, 0, 0)
            if S[i] == 'b': return (0, 1, 0, 0, 0, 0)
            if S[i] == 'c': return (0, 0, 1, 0, 0, 0)
        mid = (i + j) // 2
        l = ans(i, mid)
        r = ans(mid+1, j)
        # if (j - i + 1 == 3):
        #     print("l", i, mid, l)
        #     print("r", mid+1, j, r)
        return (
            l[0] + r[0],
            l[1] + r[1],
            l[2] + r[2],
            min(l[0] + r[3], l[3] + r[1]), #a/ab, ab/b
            min(l[1] + r[4], l[4] + r[2]),
            min(
                l[3] + r[4], # ab/bc
                l[5] + r[2], # abc/c
                l[0] + r[5]  # a/abc
            )
        )
    return ans(0, len(S)-1)

if True:
    tc = "aaabccccc"
    print(ans_dc(tc))
else:
    for r in range(1, N):
        for S in product('abc', repeat=r):
            s = ''.join(S)
            a, b, c, ab, bc, abc = ans_dc(S)
            assert(a == S.count('a'))
            assert(b == S.count('b'))
            assert(c == S.count('c'))
            assert(ab == ans_slow_ab(S))
            assert(bc == ans_slow_bc(S))
            if not (abc == ans_slow(S)):
                print(S)
                assert(False)
        print("checked", r)
