#!/usr/bin/env pypy3

def enumerate(targetSum, numDigits):
    if targetSum < 0: return []
    if numDigits == 1:
        if 0 <= targetSum <= 9: 
            return [str(targetSum)]
        else:
            return []
    
    ret = []
    for firstDigit in range(0, 10):
        for rest in enumerate(targetSum-firstDigit, numDigits-1):
            ret += [str(firstDigit) + rest]
    return ret

ans = list(map(int, enumerate(10, 8)))

K = int(input())

print(ans[K-1])
