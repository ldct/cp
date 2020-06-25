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
