#!/usr/bin/env python3

from typing import *

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        MAX_TRIM = max([len(n) for n in nums])
        
        LL = []
        
        for k in range(1, MAX_TRIM+1):
            small = [(n[-k:], i) for (i, n) in enumerate(nums)]
            small = sorted(small)
            LL += [small]
            
        ret = []

        for k, _t in queries:
            t = min(_t, MAX_TRIM)-1
            ret += [LL[t][k-1]]
                    
        return [r[1] for r in ret]

s = Solution()

print(s.smallestTrimmedNumbers(
    ["102","473","251","814"],
    [[1,1],[2,3],[4,2],[1,2]]
))