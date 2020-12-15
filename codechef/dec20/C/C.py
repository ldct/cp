#!/usr/bin/env pypy3

from functools import lru_cache

@lru_cache(None)
def mp(K, arr):
    if K == 0: return arr
    ap = []
    for p in range(max(arr).bit_length()+2):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                mask = 2**p
                new_arr = list(arr)
                new_arr[i] ^= mask
                new_arr[j] ^= mask

                ap += [mp(K-1, tuple(new_arr))]
    return min(ap)

def ans(K, arr):

    arr = arr[:]

    i = 0
    while arr[i] == 0 and i < len(arr)-1: i += 1

    while i < len(arr)-1 and K > 0:

        # print(K, arr, i)

        mask = 2**(arr[i].bit_length()-1)
        j = i+1
        while j < len(arr)-1 and (arr[j] & mask == 0):
            j += 1

        arr[i] ^= mask
        arr[j] ^= mask

        while arr[i] == 0 and i < len(arr)-1: i += 1

        K -= 1

    K = K % 2

    if K == 0: return arr

    if len(arr) > 2: return arr

    assert(len(arr) == 2)

    arr[0] ^= 1
    arr[1] ^= 1

    return arr


for _ in range(int(input())):
    N, K = input().split()
    K = int(K)
    A = list(map(int, input().split()))
    print(*ans(K, A))

# import random
# for _ in range(10000):
#     N = 2
#     K = random.randint(1, 5)
#     A = [random.randint(1, 10) for _ in range(N)]
#
#     ans(K,A)
#
#     if tuple(ans(K,A)) != mp(K,tuple(A)):
#         print(K, A, ans(K, A), mp(K,tuple(A)))
