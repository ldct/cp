#!/usr/bin/env pypy3

class DenseBlock:
    def __init__(self, block):
        self.block = block
    def getSum(self, l, r):
        assert(0 <= l <= r <= len(self))
        return sum(self.block[l:r])
    def __len__(self):
        return len(self.block)

class SumBlock:
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def getSum(self, l, r):
        assert(0 <= l <= r <= len(self))
        m = len(self.b1) - l
        if m < 0:
            return self.b2.getSum(l - len(self.b1), r - len(self.b1))
        else:
            if r - len(self.b1) > 0:
                return self.b1.getSum(l, l+m) + self.b2.getSum(0, r - len(self.b1))
            else:
                return self.b1.getSum(l, r)
    def __len__(self):
        return len(self.b1) + len(self.b2)

class AllSameBlock:
    def __init__(self, val, count):
        self.val = val
        self.count = count
    def getSum(self, l, r):
        assert(0 <= l <= r <= len(self))
        return self.val * (r - l)

    def __len__(self):
        return self.count

s1 = SumBlock(DenseBlock([1,2,3,4]), DenseBlock([5,6]))
s2 = DenseBlock([1,2,3,4,5,6])

class InfiniteRepeatBlock:
    def __init__(self, block):
        self.block = block
    def getSum(self, l, r):
        block_size = len(self.block)

        left_block_id = l // block_size
        right_block_id = r // block_size

        left_id = l % block_size
        right_id = r % block_size

        if left_block_id == right_block_id:
            return self.block.getSum(left_id, right_id)

        num_full_blocks = right_block_id - left_block_id - 1

        return num_full_blocks*self.block.getSum(0, len(self.block)) + self.block.getSum(left_id, len(self.block)) + self.block.getSum(0, right_id)

import math

def ans2(a, b, l, r):
    ret = 0
    for x in range(l, r+1):
        if x % a % b != x % b % a:
            ret += 1
    return ret

def ans(a, b, l, r):
    if a > b:
        return ans(b, a, l, r)

    a = a // math.gcd(a, b)

    arr = InfiniteRepeatBlock(
        SumBlock(
            AllSameBlock(1, b),
            AllSameBlock(0,b*(a-1))
        ))

    return r - l + 1 - arr.getSum(l,r+1)

# import random
# for i in range(100):
#     a = random.randint(1, 20)
#     b = random.randint(1, 20)

#     l = random.randint(1, 100)
#     r = random.randint(l, 10000000000000000000000)

#     ans(a, b, l, r)

T = int(input())

for _ in range(T):
    a, b, q = input().split(' ')
    a = int(a)
    b = int(b)
    q = int(q)

    res = []

    for _ in range(q):
        l, r = input().split(' ')
        l = int(l)
        r = int(r)

        res += [str(ans(a, b, l, r))]
    
    print(' '.join(res))
