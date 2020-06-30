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

    alice_only_prefix = [0]
    for b in alice_only_fc:
        alice_only_prefix += [alice_only_prefix[-1] + b]

    bob_only_prefix = [0]
    for b in bob_only_fc:
        bob_only_prefix += [bob_only_prefix[-1] + b]

    neither_prefix = [0]
    for b in neither_fc:
        neither_prefix += [neither_prefix[-1] + b]

    p = min(len(both), M)
    q = 0
    r = 0
    s = 0

    # maintain K condition

    while p + q < K:
        if q == len(alice_only): break
        q += 1
    if p + q < K: return None
    while p + r < K:
        if r == len(bob_only): break
        r += 1
    if p + r < K: return None

    # maintain M condition

    while p+q+r+s < M:
        # greedily increment q,r,s
        g = dict()
        if q < len(alice_only):
            g["q"] = alice_only_fc[q]
        if r < len(bob_only):
            g["r"] = bob_only_fc[r]
        if s < len(neither):
            g["s"] = neither_fc[s]

        if len(g.keys()) == 0: return None

        to_increment = min(g, key=g.get)

        if to_increment == "q": q += 1
        if to_increment == "r": r += 1
        if to_increment == "s": s += 1

    while p+q+r+s > M:
        # greedily decrement q,r,s

        g = dict()
        if 0 < q and p + q > K:
            g["q"] = alice_only_fc[q-1]
        if 0 < r and p + r > K:
            g["r"] = bob_only_fc[r-1]
        if 0 < s:
            g["s"] = neither_fc[s-1]

        if len(g.keys()) == 0: break

        to_decrement = max(g, key=g.get)

        if to_decrement == "q": q -= 1
        if to_decrement == "r": r -= 1
        if to_decrement == "s": s -= 1
        
    if p+q+r+s > M: return None

    best_score = both_prefix[p] + alice_only_prefix[q] + bob_only_prefix[r] + neither_prefix[s]
    best_pqrs = (p,q,r,s)

    # print("starting candidate", best_score, best_pqrs)

    while p > 0:
        p -= 1

        # maintain K condition

        while p + q < K:
            if q == len(alice_only): break
            q += 1
        if p + q < K: break
        while p + r < K:
            if r == len(bob_only): break
            r += 1
        if p + r < K: break

        # maintain M condition

        while p+q+r+s < M:
            # greedily increment q,r,s
            g = dict()
            if q < len(alice_only):
                g["q"] = alice_only_fc[q]
            if r < len(bob_only):
                g["r"] = bob_only_fc[r]
            if s < len(neither):
                g["s"] = neither_fc[s]

            if len(g.keys()) == 0: break

            to_increment = min(g, key=g.get)

            if to_increment == "q": q += 1
            if to_increment == "r": r += 1
            if to_increment == "s": s += 1

        if p+q+r+s < M: break

        while p+q+r+s > M:
            # greedily decrement q,r,s

            g = dict()
            if 0 < q and p + q > K:
                g["q"] = alice_only_fc[q-1]
            if 0 < r and p + r > K:
                g["r"] = bob_only_fc[r-1]
            if 0 < s:
                g["s"] = neither_fc[s-1]

            if len(g.keys()) == 0: break

            to_decrement = max(g, key=g.get)

            if to_decrement == "q": q -= 1
            if to_decrement == "r": r -= 1
            if to_decrement == "s": s -= 1
        
        if p+q+r+s > M: break

        score = both_prefix[p] + alice_only_prefix[q] + bob_only_prefix[r] + neither_prefix[s]

        if score < best_score:
            best_score = score
            best_pqrs = (p,q,r,s)

    p,q,r,s = best_pqrs
    ret_array = []

    for i in range(p): ret_array += [both[i][1]]
    for i in range(q): ret_array += [alice_only[i][1]]
    for i in range(r): ret_array += [bob_only[i][1]]
    for i in range(s): ret_array += [neither[i][1]]

    return best_score, ret_array

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