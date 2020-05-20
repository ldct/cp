#!/usr/bin/env python3

def one(s):
    for e in s:
        return e

def threeSum(nums):

    counts = dict()
    for n in nums:
        if n not in counts: counts[n] = 0
        counts[n] += 1
        counts[n] = min(3, counts[n])

    nums = []
    for k in counts:
        nums += [k]*counts[k]

    indexesOf = dict()
    for i, n in enumerate(nums):
        if n not in indexesOf: indexesOf[n] = set()
        indexesOf[n].add(i)

    ans = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            a = nums[i]
            b = nums[j]
            target = - a - b
            if not (target in indexesOf): continue
            if tuple(sorted([a, b, target])) in ans: continue

            if len(indexesOf[target]) > 2:
                ans.add((a, b, target))
                # ans.add(tuple(sorted([
                #     a, b, target
                # ])))
            else:                    
                for k in indexesOf[target]:
                    if k in set([i, j]): continue
                    ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                
    return list(ans)

a = input().split(",")
a = list(int(x) for x in a)
print(threeSum(a))