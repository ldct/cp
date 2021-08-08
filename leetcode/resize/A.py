#!/usr/bin/env pypy3

from functools import lru_cache

def minSpaceWastedKResizing(nums, k):
    @lru_cache(None)
    def cost(x, y):

        bound = max(nums[x:y])

        ret = 0
        for n in range(x, y):
            ret += bound - nums[n]
        return ret

    @lru_cache(None)
    def ans(i, k):
        if i >= len(nums): return 0
        if k == 0: return cost(i, len(nums))
        if k < 0: return float("inf")

        ret = float("inf")

        for t in range(i+1, len(nums)):
            candidate = ans(t, k-1) + cost(i, t)

            if ret > candidate:
                ret = candidate

        return ret

    return ans(0, k)

print(minSpaceWastedKResizing([10,14,49,22,7,6,25], 2))