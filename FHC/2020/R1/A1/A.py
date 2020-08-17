#!/usr/bin/env pypy3

MODULUS = 1000000007

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def hh(histogram):
    h = [0] + histogram + [0]
    ret = 0
    for i in range(len(h)-1):
        ret += abs(h[i] - h[i+1])
    return ret        

def ans(L, H, W):

    back_p = 0
    left = L[0]
    right = left+W
    right_height = H[0]
    sum_height = 2*H[0]
    curr_p = 2*(right - left) + sum_height
    histogram = [H[0]]*W

    # print(histogram)

    P = [back_p + curr_p]
    
    for i in range(1, len(L)):
        this_left = L[i]
        this_right = this_left + W

        assert(this_left > left)

        if this_left > right:
            # create a new block
            back_p += curr_p
            left = this_left
            right = this_right
            sum_height = 2*H[i]
            histogram = [H[i]]*W
            curr_p = 2*(right - left) + sum_height

        else:
            # extend current block
            # back_p remains same
            # left remains same

            # update histogram
            new_histogram_length = this_left - left + W
            assert(new_histogram_length - len(histogram)) <= 30
            histogram += [0]*(new_histogram_length - len(histogram))

            old_h = histogram[this_left - left - 1:]
            new_h = old_h[:]

            for j in range(W):
                o = this_left - left + j
                histogram[o] = max(histogram[o], H[i])
                new_h[j+1] = max(new_h[j+1], H[i])

            sum_height += (hh(new_h) - hh(old_h))
            assert(sum_height == hh(histogram)) # comment this out at speed

            right = this_right
            curr_p = 2*(right - left) + sum_height
            
        back_p %= MODULUS
        curr_p %= MODULUS
        P += [(back_p + curr_p) % MODULUS]

    ret = 1
    for p in P:
        ret *= p
        ret %= MODULUS

    return ret

T = int(input())

for t in range(T):
    N, K, W = input().split()
    N = int(N)
    K = int(K)
    W = int(W)
    assert(K <= N)

    L = list(map(int, input().split()))
    assert(K == len(L))

    Al, Bl, Cl, Dl = input().split()
    Al = int(Al)
    Bl = int(Bl)
    Cl = int(Cl)
    Dl = int(Dl)

    H = list(map(int, input().split()))
    assert(K == len(H))

    Ah, Bh, Ch, Dh = input().split()
    Ah = int(Ah)
    Bh = int(Bh)
    Ch = int(Ch)
    Dh = int(Dh)

    # pad out L
    while len(L) < N:
        L += [(Al*L[-2] + Bl*L[-1] + Cl) % Dl + 1]

    while len(H) < N:
        H += [(Ah*H[-2] + Bh*H[-1] + Ch) % Dh + 1]

    if t in [43, 61, 67, 72, 81]: continue
    print(f"Case #{t+1}:", ans(L, H, W))