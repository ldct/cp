# TODO: this is quite slow

class AlphaDict:
    def __init__(self, initial=None):
        self.storage = [initial]*26
    def __getitem__(self, k):
        return self.storage[ord(k) - ord('a')]
    def __setitem__(self, k, v):
        self.storage[ord(k) - ord('a')] = v
    def copy(self):
        ret = AlphaDict()
        for i in range(26): ret.storage[i] = self.storage[i]
        return ret