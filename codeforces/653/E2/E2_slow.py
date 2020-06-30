#!/usr/bin/env pypy3

from sys import stdin, stdout
import heapq
 
def input():
    return stdin.readline().strip()

def ans(both, alice_only, bob_only, neither, M, K):
    both_fc = [b[0] for b in both]
    neither_fc = [b[0] for b in neither]
    alice_only_fc = [a[0] for a in alice_only]
    bob_only_fc = [b[0] for b in bob_only]
    
    both_prefix = [0]
    for b in both_fc:
        both_prefix += [both_prefix[-1] + b]

    best_candidate = float("inf")
    best_pqr = None

    for p in range(K-min(len(alice_only), len(bob_only)), len(both)+1):
        # if N == 81 and M == 81: print("p=", p)
        qr_min = K - p
        # if N == 81 and M == 81: print("qr_min=", qr_min)

        if qr_min > len(alice_only) or qr_min > len(bob_only): assert(False)
        if qr_min < 0: qr_min = 0

        rest = M - p - 2*qr_min
        # if N == 81 and M == 81: print("rest=", rest)
        rest_fc = neither_fc + alice_only_fc[qr_min:] + bob_only_fc[qr_min:]
        if not (0 <= rest <= len(rest_fc)): continue
        candidate = both_prefix[p] + sum(alice_only_fc[0:qr_min]) + sum(bob_only_fc[0:qr_min]) + sum(sorted(rest_fc)[0:rest])
        # if N == 81 and M == 81: print("candidate=", candidate)
        if candidate < best_candidate:
            best_candidate = candidate
            best_pqr = (p, qr_min, rest)

    if best_pqr is None: return None

    p, qr_min, rest = best_pqr
    indexes = []
    for i in range(p):
        indexes += [both[i][1]]

    for i in range(qr_min):
        indexes += [alice_only[i][1], bob_only[i][1]]

    for x, y in sorted(neither + alice_only[qr_min:] + bob_only[qr_min:] + both[p:])[0:rest]:
        indexes += [y]

    return best_candidate, indexes


N, M, K = input().split(' ')
N = int(N)
K = int(K)
M = int(M)

alice_only = []
bob_only = []
both = []
neither = []
inorder = []

for i in range(1,N+1):
    t, a, b = input().split(' ')
    t = int(t)
    a = int(a)
    b = int(b)

    if a == 0 and b == 0: neither += [(t, i)]
    if a == 1 and b == 1: both += [(t, i)]
    if a == 1 and b == 0: alice_only += [(t, i)]
    if a == 0 and b == 1: bob_only += [(t, i)]

    inorder += [t]

alice_only = sorted(alice_only)
bob_only = sorted(bob_only)
both = sorted(both)
neither = sorted(neither)

ret = ans(both, alice_only, bob_only, neither, M, K)

if ret is None:
    print(-1)
else:
    a, b = ret
    print(a)
    print(' '.join(map(str, b)))

    check = 0
    for idx in b:
        check += inorder[idx-1]

    assert(a == check)