#!/usr/bin/env python3

from bisect import bisect_left as lower_bound
from typing import *

def numberOfPairs(nums,target):
    # number of pairs which sum to >= target
    nums = sorted(nums)
    p1=0
    p2=len(nums)-1
    pairs=0
    while p1<p2:
        if nums[p2]+nums[p1]>=target:
            pairs+=p2-p1
            p2-=1
        else:
            p1+=1
    return pairs
 
    
    
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        
        nums = list(set(nums))
        
        nums = ["{0:b}".format(n).count('1') for n in nums]
        
        # print(nums, k, numberOfPairs(nums, k))

        ret = 2*numberOfPairs(nums, k)
        
        for n in nums:
            if 2*n >= k:
                ret += 1
        
        return ret

s = Solution()
print(s.countExcellentPairs(
    [1,2,3,1],
    3
))
print(s.countExcellentPairs(
    [1,2,4,8,16,32,64,128,256],
    2
))